# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodların Götürən Kimliyindən Aslı Olmayaraq Peysərdi

# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os

class Config:

   API_ID = int(os.getenv("API_ID", "6711429"))
   API_HASH = os.getenv("API_HASH", "0bd538e224f28d8d8047d79f09a840ae")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "6603241671:AAEqXs9f42GwLnT4EARrcKiy0-opp_ub0TU")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "AylinRobot")
   BOT_NAME = os.environ.get("BOT_NAME", "AylinRobot")
   OWNER_ID = int(os.environ.get("OWNER_ID", "571698989"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "AylinRobot") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("mongodb+srv://lucis:lucis@cluster0.hpuze.mongodb.net/lucis?retryWrites=true&w=majority")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001864613336"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "AylinRobot")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001750384884"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1001864613336"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "6e2ee8af-4c45-4a54-9f3a-cccf3b76fc95")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "AylinRobot")
   CHANNEL = os.environ.get("CHANNEL", "AylinRobot")
   SUPPORT = os.environ.get("SUPPORT", "FriendsAilesi")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/33c593637f4766883abed.mp4") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/f1caca00edcf2884d2436.jpg")
   COMMAND_PREFIXES = list(os.environ.get("COMMAND_PREFIXES", "/ ! .").split())