from Dfschinnamusic.core.bot import Dfs
from Dfschinnamusic.core.dir import dirr
from Dfschinnamusic.core.git import git
from Dfschinnamusic.core.userbot import Userbot
from Dfschinnamusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
#git()
dbb()
heroku()

app = Dfs ()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
