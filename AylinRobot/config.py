# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodların Götürən Kimliyindən Aslı Olmayaraq Peysərdi

# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os

class Config:

   API_ID = int(os.getenv("API_ID", "12349641"))
   API_HASH = os.getenv("API_HASH", "0f9159afc920f9c592df555e4b1cb73b")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "6955606859:AAHftUtcWxJAdocEnS1J4bIoBoFlRM9RblM")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "otobotrobot")
   BOT_NAME = os.environ.get("BOT_NAME", "otobotrobot")   
   OWNER_ID = int(os.environ.get("OWNER_ID","6634423600"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "thagiyev") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://nesirovq1997:qadir1997@cluster0.pavador.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002115471818"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "nezrinlogo")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1002140637128"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1002115471818"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "56ae7152-5102-4d4b-8ab7-218810c69336")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "otobotrobot")
   CHANNEL = os.environ.get("CHANNEL", "nezrinlogw")
   SUPPORT = os.environ.get("SUPPORT", "nezrinlogw")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "") 
   START_IMG = os.environ.get("START_IMG", "")
   COMMAND_PREFIXES = list(os.environ.get("COMMAND_PREFIXES", "/ ! .").split())
