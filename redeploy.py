import subprocess
from pyrogram import Client, filters
from Devine import app, LORD as OWNER_ID

@app.on_message(filters.command("redeploy") & filters.user(OWNER_ID))
async def redeploy(client, message):
    msg = await message.reply("Starting bot redeployment process...")

    try:
        await msg.edit("Pulling the latest changes from GitHub...")
        pull_process = subprocess.run(
            ["git", "pull", "origin", "main"],
            capture_output=True, text=True
        )
        if pull_process.returncode != 0:
            raise Exception(f"Git pull failed: {pull_process.stderr}")

        await msg.edit("Deploying changes to Heroku...")
        deploy_process = subprocess.run(
            ["heroku", "git:remote", "-a", "your-heroku-app-name"], 
            capture_output=True, text=True
        )
        if deploy_process.returncode != 0:
            raise Exception(f"Heroku remote setup failed: {deploy_process.stderr}")

        deploy_process = subprocess.run(
            ["git", "push", "heroku", "main"], 
            capture_output=True, text=True
        )
        if deploy_process.returncode != 0:
            raise Exception(f"Git push to Heroku failed: {deploy_process.stderr}")

        await msg.edit("Restarting the Heroku app...")
        restart_process = subprocess.run(
            ["heroku", "ps:restart", "--app", "your-heroku-app-name"], 
            capture_output=True, text=True
        )
        if restart_process.returncode != 0:
            raise Exception(f"Heroku restart failed: {restart_process.stderr}")

        await msg.edit("Bot redeployment completed successfully!")

    except Exception as e:
        await msg.edit(f"Error during redeployment: {str(e)}")
