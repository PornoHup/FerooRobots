# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodların Götürən Kimliyindən Aslı Olmayaraq Peysərdi

# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os

class Config:

   API_ID = int(os.getenv("API_ID", "8953338"))
   API_HASH = os.getenv("API_HASH", "fe21f223cb02d8f7c1cbda651f553a45")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "1528782615:AAFtWtheWNjoNBEJnE-M_32xKbiIUpD46U0")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "FidanRobot")
   BOT_NAME = os.environ.get("BOT_NAME", "FidanRobot")
   OWNER_ID = int(os.environ.get("OWNER_ID","5731647757"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "Hesenov_H") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001886156935"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "FidanRobotPlaylis")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001824771162"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1001820370604"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "c59d490e-5f1a-4469-a685-101abff455db")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "HUSEYN")
   CHANNEL = os.environ.get("CHANNEL", "HuseynH")
   SUPPORT = os.environ.get("SUPPORT", "HuseynH")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/7b01cef8f87059387d91b.jpg") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/7b01cef8f87059387d91b.jpg")