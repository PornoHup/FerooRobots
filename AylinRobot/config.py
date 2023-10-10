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
   BOT_TOKEN = os.getenv("BOT_TOKEN", "6552355594:AAE-0v09aZhXhgeWGz1weZYQJFpifO7b-I8")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "GulfidanRobot")
   BOT_NAME = os.environ.get("BOT_NAME", "GulfidanRobot")   
   OWNER_ID = int(os.environ.get("OWNER_ID","5898049921"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "Tiri_viri_isler") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001949909329"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "gulfidanplayist")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001857095101"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1001862865565"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "05a017d5-e3e5-424d-941f-3e60645e3141")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "Tiri_viri_isler")
   CHANNEL = os.environ.get("CHANNEL", "Tiri_viri_isler")
   SUPPORT = os.environ.get("SUPPORT", "Sohbet_otagi")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/642139ca03a36ecb35709.jpg") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/fe20477e7dbccf5b83a02.jpg")
   COMMAND_PREFIXES = list(os.environ.get("COMMAND_PREFIXES", "/ ! .").split())
