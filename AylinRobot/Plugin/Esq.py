from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from AylinRobot.config import Config
from AylinRobot import AylinRobot as app

ESQ_FAIZ = ["0%", "10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]

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
            eşq_faizi = random.choice(ESQ_FAIZ)
            await message.reply(f"Eşq Faizi Hesablandı\n\n{message.reply_to_message.from_user.mention} + {message.from_user.mention} = ❤\nEşq Faizi: {eşq_faizi}")
    except Exception:
        await message.reply("⚠️ XƏTA")