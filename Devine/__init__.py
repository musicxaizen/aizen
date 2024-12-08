from Devine.root.bot import Devine
from Devine.root.dir import dirr
from Devine.root.userbot import Userbot
from Devine.misc import dbb, heroku
from .logging import LOGGER

dirr()
dbb()
heroku()

app = Devine()
userbot = Userbot()
LORD = 7472465398

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
