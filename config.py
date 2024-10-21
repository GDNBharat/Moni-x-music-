import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "28362850"))
API_HASH = getenv("API_HASH", "34f9cb93364db16fc45d003e4c81d97a")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7151436558:AAE5HzbAl7F6IBxAUVsNOHqjy9l0XOHVW9E")
# Get your MongoDB URI from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://VamsixD:VamsixD@vamsi.x7gyybv.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat ID of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002141779241"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6896043885))

# Fill these variables if you're deploying on Heroku.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/dattudd/Anonxmusic-")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/DFSchinnaop")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DFSchinnaop")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False").lower() in ("true", "1", "t")

# Get these credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET")

# Maximum limit for fetching playlist's tracks from YouTube, Spotify, Apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# Load session strings from environment variables
STRING1 = getenv("STRING_SESSION",  "BQGwyGIARcFn4SqDMwGXF_Dgnyr3vtmzPUbKIgVc-8aphGrcKXOJNVMoG78jhI0kSIfeAV12DkJLCNfGaBWhL8SK-_fXN6ivEqm9MOLEmnjtQOkUTdAO1hKOXX4HCyYK_7_CUN4n-gttIvB7aP3TNY0KvS-GfbUOYGzFEvLoyIbJiBn9VSbqL56gbZJX4G4P4o1yviNEDeA6gB2Pse6CvrT8zSwJBzdLCP_mdy5HvJHdVl2xaYlF4xWwzE7PhCvCbjaptk0xbZRZLBQ-HWZwtZ3gxLV43ksQ_W5io4UgsrGr2IIbTr2uWDyVoO45A9AobdrYtl_yCNGfIJwG3DRbc6i-ALZTRwAAAAHETnMdAA")
STRING2 = getenv("STRING_SESSION2",) 
STRING3 = getenv("STRING_SESSION3",)
STRING4 = getenv("STRING_SESSION4",)
STRING5 = getenv("STRING_SESSION5",) 

# Ensure the environment variables are loaded
if not all([STRING1]):
    raise ValueError("One or more STRING_SESSION environment variables are missing")


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/8d7b534e34e13316a7dd2.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/file/ca95213f8c1dd9a19c239.jpg")
PLAYLIST_IMG_URL = "https://telegra.ph/file/8d7b534e34e13316a7dd2.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT_MIN = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL URL is incorrect. Please ensure it starts with https://")

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Your SUPPORT_CHAT URL is incorrect. Please ensure it starts with https://")
