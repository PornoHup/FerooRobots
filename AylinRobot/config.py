# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodların Götürən Kimliyindən Aslı Olmayaraq Peysərdi

# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os

class Config:

   API_ID = int(os.getenv("API_ID", "26090016"))
   API_HASH = os.getenv("API_HASH", "5b842f9801712684f2b98d70ead6538d")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "GunelBot")
   BOT_NAME = os.environ.get("BOT_NAME", "GunelBot")   
   OWNER_ID = int(os.environ.get("OWNER_ID","6471021703"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "The_ferid") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://public:abishnoimf@cluster0.rqk6ihd.mongodb.net/?retryWrites=true&w=majority")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002140822720"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "GunelPlaylist")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1002139433704"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1002055465224"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "92d7b226-f553-455a-9ecc-794a5204b868")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "The_ferid")
   CHANNEL = os.environ.get("CHANNEL", "FerooResmi")
   SUPPORT = os.environ.get("SUPPORT", "GunelSupport")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/ae50093941650e0e20cc2.jpg") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/ae50093941650e0e20cc2.jpg")
   COMMAND_PREFIXES = list(os.environ.get("COMMAND_PREFIXES", "/ ! .").split())
