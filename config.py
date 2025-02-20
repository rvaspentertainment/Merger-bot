import os


class Config(object):
    API_HASH = os.environ.get("3d1ab21b51395b1d8297932e7a264e96")
    BOT_TOKEN = os.environ.get("7681701929:AAH4tmQejPQYmJ4Os-F4o_qknMI3o0NZSZc")
    TELEGRAM_API = os.environ["7681701929"]
    OWNER = os.environ.get("Ghost")
    OWNER_USERNAME = os.environ.get("@NeverStopI")
    PASSWORD = os.environ.get("PASSWORD")
    DATABASE_URL = os.environ.get("DATABASE_URL")
    LOGCHANNEL = os.environ.get("LOGCHANNEL")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
