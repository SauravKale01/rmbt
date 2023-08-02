import os

class Config(object):
    BANNED_USERS = []
    DOWNLOAD_LOCATION = "./DOWNLOADS" 
    API_ID = int(os.environ.get("API_ID", 19099900))
    API_HASH = os.environ.get("API_HASH" "2b445de78e5baf012a0793e60bd4fbf5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6308859474:AAEOQpio4xzMDMUVf7oN4GEPn206i_r_jbw")
    OWNER_ID = int(os.environ.get("OWNER_ID", "6265459491"))
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", None)
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://sonu55:sonu55@cluster0.vqztrvk.mongodb.net/?retryWrites=true&w=majority")
