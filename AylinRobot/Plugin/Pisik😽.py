# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
import time
from time import time
import random
from random import choice
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from pyrogram import filters
from helpers.filters import command, other_filters
from AylinRobot.config import Config


photolist = ["https://telegra.ph/file/1559957902ea74780464c.jpg","https://telegra.ph/file/319dc0767d7202c519111.jpg","https://telegra.ph/file/826544346d36c4a4e3530.jpg","https://telegra.ph/file/7ce7b1353b840aa6cca0f.jpg","https://telegra.ph/file/5cc61ddbe6066c17f3622.jpg","https://telegra.ph/file/ab833fc88c1bf1fa686cb.jpg","https://telegra.ph/file/0a6737de0e34a998ffdf5.jpg","https://telegra.ph/file/6e7bb2d3f9e7e8ed2f3c0.jpg","https://telegra.ph/file/3b9a14eff0434a052bb31.jpg","https://telegra.ph/file/02fb564566106642ea28e.jpg","https://telegra.ph/file/7acca37265a959623e723.jpg","https://telegra.ph/file/be7a6e215bf60707ae4ef.jpg","https://telegra.ph/file/9743726509a51a6f8020a.jpg","https://telegra.ph/file/6d3dbd498e68adc5f8950.jpg","https://telegra.ph/file/787ee0608b5b3d36fb698.jpg","https://telegra.ph/file/5ae7ea53c70935954c9e1.jpg","https://telegra.ph/file/259fbe1b0c33ec510dcc4.jpg","https://telegra.ph/file/dc65fd499a2d42b3154dd.jpg","https://telegra.ph/file/944eb25f995efa27bbf2f.jpg","https://telegra.ph/file/c796d475a84b65ac29d3f.jpg","https://telegra.ph/file/259fbe1b0c33ec510dcc4.jpg","https://telegra.ph/file/494a80d84078ce824a8a0.jpg","https://telegra.ph/file/726fbdefabdfe4c4f492d.jpg","https://telegra.ph/file/cddafd9b6dcaa9657877a.jpghttps://","https://telegra.ph/file/494a80d84078ce824a8a0.jpg","https://telegra.ph/file/ac760227e8857a2328ac1.jpg","https://telegra.ph/file/afe034f8b5a423640875d.jpg","https://telegra.ph/file/d9202cf4f3baf0325e3b2.jpg","https://telegra.ph/file/44e800b02c583d41b8cc8.jpg","https://telegra.ph/file/abfcfb9cb80afc82e0b64.jpg","https://telegra.ph/file/abfcfb9cb80afc82e0b64.jpg","https://telegra.ph/file/40eb1dfe6f41f81db4639.jpg","https://telegra.ph/file/40eb1dfe6f41f81db4639.jpg","https://telegra.ph/file/7b7a94e648601b3380e85.jpg","https://telegra.ph/file/d9202cf4f3baf0325e3b2.jpg","https://telegra.ph/file/12af74ede532c0fe14001.jpg","https://telegra.ph/file/57ad118f1b38fb8202405.jpg","https://telegra.ph/file/76b8b8cebc019ec865410.jpg","https://telegra.ph/file/8fa7af43faf05bed98bc5.jpg","https://telegra.ph/file/7ed57eb91cd269e17bf81.jpg","https://telegra.ph/file/37d7c14b9beb9b8aa29e3.jpg","https://telegra.ph/file/261135ba2037103dfe263.jpg","https://telegra.ph/file/59c28bc5bd9851863c874.jpg","https://telegra.ph/file/5e46e5f5cf4edc4606abf.jpg","https://telegra.ph/file/37d7c14b9beb9b8aa29e3.jpg","https://telegra.ph/file/2e8cbb87b81ced79f544e.jpg","https://telegra.ph/file/1ccb1b6373a77b56eda5f.jpg","https://telegra.ph/file/b542d4af244e95511bf69.jpg","https://telegra.ph/file/b542d4af244e95511bf69.jpg","https://telegra.ph/file/8cd0abbd784158a5f08b3.jpg","https://telegra.ph/file/db4b09971fd8c13a87a29.jpg","https://telegra.ph/file/b57fe567110e3f4a7235f.jpg","https://telegra.ph/file/c629dabbdbfc64bf0b175.jpg","https://telegra.ph/file/d34b9ec1241cb970f11f1.jpg","https://telegra.ph/file/ca7dc164d7c44fe6f2920.jpg","https://telegra.ph/file/953bf56b93bb138f42fd6.jpg","https://telegra.ph/file/ca73c497b453d4486ad28.jpg","https://telegra.ph/file/b6c1e2295f6399635d4bb.jpg","https://telegra.ph/file/dc0d350db68fd6fdce8fd.jpg","https://telegra.ph/file/be35e430806a265acfd60.jpg","https://telegra.ph/file/be35e430806a265acfd60.jpg","https://telegra.ph/file/8faf22942cbbef794010b.jpg","https://telegra.ph/file/833bbd259911fff1386f2.jpg", "https://telegra.ph/file/f07ee1a668eb8eb144a3a.jpg", "https://telegra.ph/file/8f696ed4a1d50a30e0450.jpg", "https://telegra.ph/file/8c80f4b3cd36874284698.jpg", "https://telegra.ph/file/5ae4cb0fddd1e09ce8cdf.jpg", "https://telegra.ph/file/36ced5c8e781972bcb1e5.jpg", "https://telegra.ph/file/1f3023d99f7d17507b72e.jpg", "https://telegra.ph/file/0c61832eddd6289c82f12.jpg", "https://telegra.ph/file/b5ab47c5549f44a092a2f.jpg", "https://telegra.ph/file/a243d1dbe8c94d9bdb32a.jpg", "https://telegra.ph/file/135262d7c98473930e0e2.jpg", "https://telegra.ph/file/fafd921f750fb5175d965.jpg", "https://telegra.ph/file/4f4c1c4aa79ef463c91da.jpg", "https://telegra.ph/file/53730fc3546cc567b4341.jpg", "https://telegra.ph/file/f56c00e5798e58376f94b.jpg", "https://telegra.ph/file/162903ff27c69928acac6.jpg", "https://telegra.ph/file/5f213a1da87f02855372b.jpg", "https://telegra.ph/file/02baffd157f60b3ab9afd.jpg", "https://telegra.ph/file/fce9a6d39d3819f4831c2.jpg", "https://telegra.ph/file/7ff09c63bb33f3d424ce9.jpg", "https://telegra.ph/file/bdbc0e479f81ffc4f73fd.jpg", "https://telegra.ph/file/ded5644c427a1b490e87c.jpg", "https://telegra.ph/file/43368c0f76853d6c9112f.jpg", "https://telegra.ph/file/27a95cf6312cf668664f9.jpg", "https://telegra.ph/file/33f9923482a2f698daa38.jpg", "https://telegra.ph/file/8094d87d6fbc946127c80.jpg", "https://telegra.ph/file/804167af66ad501c4661a.jpg", "https://telegra.ph/file/4b54b8e071278fa9cafa6.jpg", "https://telegra.ph/file/b1bf37b44f04eb4ce5b4a.jpg", "https://telegra.ph/file/34a5a44e47c8717570bd7.jpg", "https://telegra.ph/file/f10d449a9c6bc2350fcb1.jpg", "https://telegra.ph/file/3b84fd3fbb7db95a7eb6c.jpg", "https://telegra.ph/file/d217d741374c68d12c072.jpg", "https://telegra.ph/file/7ca7c0814b58eec95a1fd.jpg", "https://telegra.ph/file/3e6857957287e0d3c704f.jpg", "https://telegra.ph/file/e0f4f9e211d465a6776ee.jpg", "https://telegra.ph/file/6045272462b55bb09303b.jpg"] 
 
 
 

@app.on_message(filters.command("pisik") & ~filters.edited)
async def test_bot(bot: app, m: Message):
    start = time()
    replymsg = await m.reply_text("**❤ Rondom Bir Pişik Şəkili Seçilir...**")
    end = round(time() - start, 2)
    photo = random.choice(photolist)
    text = f"❤️ **{Config.BOT_USERNAME} Sizin Üçün Rondom Bir Pişik Şəkili Seçdi**"
    await bot.send_photo(m.chat.id, photo=photo, caption=text)
    await replymsg.delete()