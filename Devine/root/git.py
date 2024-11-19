import asyncio
import shlex
from typing import Tuple

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

import configuration

from ..logging import LOGGER


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(install_requirements())


def hide_sensitive_info(message: str) -> str:
    # Function to hide sensitive information in messages
    return message.replace(configuration.UPSTREAM_REPO, "<hidden>")


def git():
    REPO_LINK = configuration.UPSTREAM_REPO
    if configuration.GIT_TOKEN:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        UPSTREAM_REPO = f"https://{GIT_USERNAME}:{configuration.GIT_TOKEN}@{TEMP_REPO}"
    else:
        UPSTREAM_REPO = configuration.UPSTREAM_REPO

    try:
        repo = Repo()
        LOGGER(__name__).info("Git Client Found [VPS DEPLOYER]")
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("origin", UPSTREAM_REPO)
        origin.fetch()
        repo.create_head(configuration.UPSTREAM_BRANCH, origin.refs[configuration.UPSTREAM_BRANCH])
        repo.heads[configuration.UPSTREAM_BRANCH].set_tracking_branch(
            origin.refs[configuration.UPSTREAM_BRANCH]
        )
        repo.heads[configuration.UPSTREAM_BRANCH].checkout()
    except GitCommandError as e:
        LOGGER(__name__).error(f"Invalid Git Command: {e}")
        return

    try:
        origin = repo.remote("origin")
    except ValueError:
        origin = repo.create_remote("origin", UPSTREAM_REPO)
    
    origin.fetch(configuration.UPSTREAM_BRANCH)
    
    try:
        origin.pull(configuration.UPSTREAM_BRANCH)
    except GitCommandError as e:
        repo.git.reset("--hard", "FETCH_HEAD")
        LOGGER(__name__).error(f"Error pulling from upstream: {e}")

    install_req("pip3 install --no-cache-dir -r requirements.txt")
    LOGGER(__name__).info(f"Fetching updates from upstream repository: {hide_sensitive_info(UPSTREAM_REPO)}")


# Call the git function
git()
