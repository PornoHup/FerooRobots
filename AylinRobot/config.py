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
   BOT_TOKEN = os.getenv("BOT_TOKEN", "6901117215:AAF-o0-RA9Grm5_tYBcms-nFhvvdIXiBpOI")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "FerooRobot")
   BOT_NAME = os.environ.get("BOT_NAME", "FerooRobot")   
   OWNER_ID = int(os.environ.get("OWNER_ID","6297494131"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "The_ferid") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "feroologin"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "ferooplaylist")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1002091369970"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "feroobanned"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "05a017d5-e3e5-424d-941f-3e60645e3141")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "The_ferid")
   CHANNEL = os.environ.get("CHANNEL", "FerooResmi")
   SUPPORT = os.environ.get("SUPPORT", "sah_team")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/642139ca03a36ecb35709.jpg") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/938bf884f0072c2a612b9.jpg")
   COMMAND_PREFIXES = list(os.environ.get("COMMAND_PREFIXES", "/ ! .").split())
