from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from AylinRobot.config import Config
from AylinRobot import AylinRobot as app
from mesaj.bot import ESQ_FAIZ



@app.on_message(filters.command(["esq", "eşq"], [".", "!", "@", "/"]))
async def get_id(client, message):
    try:

        if (not message.reply_to_message) and (message.chat):
            await message.reply(f"✔ Bu Əmri Hər Hansı Bir Nəfərin Mesajına Yanıt Verərək İsdifadə Edin.")
          
        elif not message.reply_to_message:
            await message.reply(f"⚠️ XƏTA") 

        elif message.reply_to_message.forward_from_chat:
            await message.reply(f"⚠️XƏTA\n🚫 Bu Əmr Kanal Üzrə Keçərli Deyil")

        elif message.reply_to_message.forward_from:
            await message.reply(f"⚠️ XƏTA")

        elif message.reply_to_message.forward_sender_name:
            await message.reply("⚠️ XƏTA")

        else:
            await message.reply(f"Eşq Faizi Hesablandı\n\n{message.reply_to_message.from_user.mention} + {message.from_user.mention} = ❤\nEşq Faizi:-  {random.choice(ESQ_FAIZ)}")

    except Exception:
            await message.reply("⚠️  XƏTA")
