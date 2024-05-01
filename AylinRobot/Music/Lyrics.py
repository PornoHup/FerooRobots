# @AylinRobot
#@MusicAzBot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Roponu Satışa Qoyan Konkret Peysərdi

from AylinRobot import AylinRobot as app
from pyrogram import Client, filters
from AylinRobot.config import Config
import os, youtube_dl, requests, aiohttp, wget, time, yt_dlp, lyricsgenius
from youtube_search import YoutubeSearch
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message, User
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message, CallbackQuery
)


@app.on_message(filters.command(["lyrics"]))
async def lyrics(_, message: Message):
    m = await message.delete()  
    if len(message.command) < 2:
        return await message.reply_text("**İstifadə:**\n\n/lyrics [ Musiqi Adı]")
    m = await message.reply_text("✍️ Muzik sözleri axtarılır")
    query = message.text.split(None, 1)[1]
    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    y.verbose = False
    S = y.search_song(query, get_full_info=False)
    if S is None:
        return await m.edit("Muzik sözleri bulunamadı: 🥹")
    xxx = f"""
**🙋‍♀️ Yükleyen {Config.BOT_USERNAME}**
**🎶 Aranan Muzik:-** __{query}__
 **📖 Bulunan Muzik Sözleri:-** __{S.title}__
 **✍️ Sanatçı:-** {S.artist}
 **📄 __Muzik sözleri:__**

{S.lyrics}"""
    if len(xxx) > 4096:
        await m.delete()
        filename = "lyrics.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(xxx.strip()))
        await message.reply_document(
            document=filename,
            caption=f"**Sözlər çox olduğundan fayl edib atdım...:**\n\n`Lyrics`",
            quote=False,
        )
        os.remove(filename)
    else:
        await m.edit(xxx)
