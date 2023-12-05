# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodların Götürən Kimliyindən Aslı Olmayaraq Peysərdi

# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os

class Config:

   API_ID = int(os.getenv("API_ID", "14965050"))
   API_HASH = os.getenv("API_HASH", "38bab2dab10fc1b6a9ba0bf683fd7048")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "6471267140:AAGCzsUbDwtfY9CXEn9RYhVHvP7G6N9UqVg")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "GunayRoBot")
   BOT_NAME = os.environ.get("BOT_NAME", "Gunay🤍")   
   OWNER_ID = int(os.environ.get("OWNER_ID","6859815593"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "GtaElgun") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://public:abishnoimf@cluster0.rqk6ihd.mongodb.net/?retryWrites=true&w=majority")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002057655400"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "GunayPlaylist")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001884377794"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1002032677567"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "92d7b226-f553-455a-9ecc-794a5204b868")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "GunayRoBot")
   CHANNEL = os.environ.get("CHANNEL", "ElikoResmi")
   SUPPORT = os.environ.get("SUPPORT", "OliqarxTeam")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/bea331e8e4921238cb954.jpg") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/bea331e8e4921238cb954.jpg")
   COMMAND_PREFIXES = list(os.environ.get("COMMAND_PREFIXES", "/ ! .").split())
