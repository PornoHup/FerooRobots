# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodların Götürən Kimliyindən Aslı Olmayaraq Peysərdi

# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os

class Config:

   API_ID = int(os.getenv("API_ID", ""))
   API_HASH = os.getenv("API_HASH", "")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
   BOT_NAME = os.environ.get("BOT_NAME", "")   
   OWNER_ID = int(os.environ.get("OWNER_ID",""))
   OWNER_NAME = os.environ.get("OWNER_NAME", "") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", ""))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", ""))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "05a017d5-e3e5-424d-941f-3e60645e3141")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "")
   CHANNEL = os.environ.get("CHANNEL", "")
   SUPPORT = os.environ.get("SUPPORT", "")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/642139ca03a36ecb35709.jpg") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/fe20477e7dbccf5b83a02.jpg")
   COMMAND_PREFIXES = list(os.environ.get("COMMAND_PREFIXES", "/ ! .").split())
