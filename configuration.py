import re 
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

def get_env_var(var_name, default=None, required=False):
    value = getenv(var_name, default)
    if required and value is None:
        raise ValueError(f"Environment variable {var_name} is required but not set.")
    return value
    
API_ID = 24885991

API_HASH = "81b0b8063ee70c1475e95e58d06e15ee"

BOT_TOKEN = "7404841712:AAFAdAH6nCbgBSOH9XfT7GW1F8ZyiulgvDE"

BOT_ID = 7404841712

BOT_USERNAME = "soul_musixbot"

MONGO_DB_URI = "mongodb+srv://aizenxmongo:0vmRucmzTP26cKTs@cluster0.nlvql.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(get_env_var("DURATION_LIMIT", 500000))

LOGGER_ID = int(get_env_var("LOGGER_ID", -1002070231017))

LOG_CHANNEL_ID = -1002303365261

OWNER_ID = 6806897901

SPECIAL_USER_ID = 7472465398

HEROKU_APP_NAME = "developer4"

HEROKU_API_KEY = None

UPSTREAM_REPO = None

UPSTREAM_BRANCH = None

GIT_TOKEN = None

SUPPORT_CHANNEL = "https://t.me/soul_x_network"

SUPPORT_CHAT = "https://t.me/soul_x_society"

AUTO_LEAVING_ASSISTANT = bool(get_env_var("AUTO_LEAVING_ASSISTANT", False))

SPOTIFY_CLIENT_ID = get_env_var("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")

SPOTIFY_CLIENT_SECRET = get_env_var("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

PLAYLIST_FETCH_LIMIT = int(get_env_var("PLAYLIST_FETCH_LIMIT", 25))

TG_AUDIO_FILESIZE_LIMIT = int(get_env_var("TG_AUDIO_FILESIZE_LIMIT", 2147483648))
TG_VIDEO_FILESIZE_LIMIT = int(get_env_var("TG_VIDEO_FILESIZE_LIMIT", 2147483648))


STRING1 = "BQF7uucAI13M7TdI1AG0zMpO3HVOojfDeoiDHER86vBtIkSzW485otS6VQ1HCDyiSBEJ-_7rYWsKDNitE8ClO4PjQyh5MIiGDd9Ma5m7xJf7ie1tSW5YYiczTkDxi6MW2ALLv5dfDGDsx24IJRsuOxyCiv7ylo8XLb8YOt8xbjiWpDQegj9Hl0Jhv2FtGX64s-iR9E4izix1NcyM3Y3-YI1TRR-V2AepWu52A8gmkPZN3j46b3bALbhfqw2YPtd-BMiDrnXdwZghrTD__ussZjnnnf5jn_LBZoZmPSFeWTfU2F05-vrCxq-SoPZM53KuolvwQbSjs9WjZ8UB0HF5iTS0w45dTAAAAAGXyEqDAA"
STRING2 = get_env_var("STRING_SESSION2", None)
STRING3 = get_env_var("STRING_SESSION3", None)
STRING4 = get_env_var("STRING_SESSION4", None)
STRING5 = get_env_var("STRING_SESSION5", None)


filter_users = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = get_env_var("START_IMG_URL", "https://envs.sh/KZQ.jpg")
PING_IMG_URL = get_env_var("PING_IMG_URL", "https://envs.sh/KZQ.jpg")
PLAYLIST_IMG_URL = "https://envs.sh/KZQ.jpg"
STATS_IMG_URL = "https://envs.sh/KZQ.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/KZQ.jpg"
TELEGRAM_VIDEO_URL = "https://envs.sh/KZQ.jpg"
STREAM_IMG_URL = "https://envs.sh/KZQ.jpg"
SOUNCLOUD_IMG_URL = "https://envs.sh/KZQ.jpg"
YOUTUBE_IMG_URL = "https://envs.sh/KZQ.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/KZQ.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/KZQ.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://envs.sh/KZQ.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://")

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit("[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://")
