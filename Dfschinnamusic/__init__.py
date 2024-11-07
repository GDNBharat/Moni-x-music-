from Dfschinnamusic.core.bot import Dfs
from Dfschinnamusic.core.dir import dirr
from Dfschinnamusic.core.git import git
from Dfschinnamusic.core.userbot import Userbot
from Dfschinnamusic.misc import dbb, heroku

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Bot Client
app = Dfs()

# Assistant Client
userbot = Userbot()

from .platforms import PlaTForms

Platform = PlaTForms()
HELPABLE = {}

