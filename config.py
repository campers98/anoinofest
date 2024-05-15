import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "24086498"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv(
    "MONGO_DB_URI",
    "mongodb://clve73lfu001ha4me1al6gw90:UTfT7DjJGjwyvbdXaM1hDrVj@104.251.218.202:9013/?readPreference=primary&ssl=false",
)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 360))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1001975251757"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 5259884546))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/campers98/anoinofest",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SVD_Squad_Gamerz")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/SVDSupportgroup")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "e60cd7a829cc4a80804553a20c216379")
SPOTIFY_CLIENT_SECRET = getenv(
    "SPOTIFY_CLIENT_SECRET", "c9d6d953a45b47aea4f56a0acb45ece2"
)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv(
    "STRING_SESSION",
    "BQGqlzEAUAGdK4t1MkzmeG7ivE3ER9AutwZP9YYnXsEdkWnZR9aINO1o7USh8_7vYkLbX51mcAX4Ivrmi56p529gsFojB8YhLn5CypH36b1hLLuIV51oNpp3Rj28lhQ_4f0nFlz9IYH9cfjXtFxS7ec1b918Vjf6EkMNTlEwXg3XKwBkOcVjuJyZM_Rkfoc2sCTzaYa4yMbCWhApz8h4RX6oEFrztnXLVLEgEsZRVeMZbg6Sx6clJhUr_CH9_ITRG3uUUYjbwgbi0HWavPrjgBbDornEGzK2eTMYjFJ_ICqO74ERvxzlIOcdmPexKXTSlOw2X9PtZjllXI7BqiRy-6Cdi_4EewAAAAFXTCi3AA",
)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/227d133eaac85b0e538d1.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/86f81220c410743f1e1b1.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/049da2a0678db379dc6ca.jpg"
STATS_IMG_URL = "https://telegra.ph/file/9349a004446e5e94abd6b.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/86f81220c410743f1e1b1.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/86f81220c410743f1e1b1.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/86f81220c410743f1e1b1.jpg"
SOUNCLOUD_IMG_URL = "assets/Soundcloud.jpeg"
YOUTUBE_IMG_URL = "assets/Youtube.jpeg"
SPOTIFY_ARTIST_IMG_URL = "assets/SpotifyArtist.jpeg"
SPOTIFY_ALBUM_IMG_URL = "assets/SpotifyAlbum.jpeg"
SPOTIFY_PLAYLIST_IMG_URL = "assets/SpotifyPlaylist.jpeg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
