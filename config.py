import os

TELEGRAM_API = int(os.getenv("TELEGRAM_API"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER = int(os.getenv("OWNER"))
OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
PASSWORD = os.environ.get("PASSWORD")
LOGCHANNEL = os.environ.get("LOGCHANNEL")  # Add channel id as -100 + Actual ID
GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
IS_PREMIUM = False
MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
