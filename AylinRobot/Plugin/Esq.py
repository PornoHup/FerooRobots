from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from AylinRobot.config import Config
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters


@app.on_message(filters.command(["esq", "eşq"], [".", "!", "@", "/"]))
async def calculate_love(client, message):
    try:
        if not message.reply_to_message or not message.chat:
            await message.reply("✔ Bu Əmri Hər Hansı Bir Nəfərin Mesajına Yanıt Verərək İsdifadə Edin.")
            return

        def hesapla_esq_faizi():
            eşq_faizi = random.randint(0, 100)
            return eşq_faizi

        reply_message = message.reply_to_message
        if reply_message.forward_from_chat or reply_message.forward_from or reply_message.forward_sender_name:
            await message.reply("⚠️ Bu Əmr Keçərli Deyil")
        else:
            eşq_faizi = hesapla_esq_faizi()
            response = f"Eşq Faizi Hesablandı\n\n{reply_message.from_user.mention} + {message.from_user.mention} = ❤\nEşq Faizi: {eşq_faizi}%"
            await message.reply(response)
    except Exception as e:
        await message.reply("⚠️ XƏTA")