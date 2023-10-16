from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from AylinRobot.config import Config
from AylinRobot import AylinRobot as app

ESQ_FAIZ = ['10%', '11%', '12%', '13%', '14%', '15%', '16%', '17%', '18%', '19%', '20%', '21%', '22%', '23%', '24%', '25%', '26%', '27%', '28%', '29%', '30%', '31%', '32%', '33%', '34%', '35%', '36%', '37%', '38%', '39%', '40%', '41%', '42%', '43%', '44%', '45%', '46%', '47%', '48%', '49%', '50%', '51%', '52%', '53%', '54%', '55%', '56%', '57%', '58%', '59%', '60%', '61%', '62%', '63%', '64%', '65%', '66%', '67%', '68%', '69%', '70%', '71%', '72%', '73%', '74%', '75%', '76%', '77%', '78%', '79%', '80%', '81%', '82%', '83%', '84%', '85%', '86%', '87%', '88%', '89%', '90%', '91%', '92%', '93%', '94%', '95%', '96%', '97%', '98%', '99%', '100%']

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
            await message.reply(f"Eşq Faizi Hesablandı\n\n{message.reply_to_message.from_user.mention} + {message.from_user.mention} = ❤\nEşq Faizi:-  {random.choice(ESQ_FAIZ)}")
    except Exception:
        await message.reply("⚠️ XƏTA")
