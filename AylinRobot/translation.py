# @AylinRobot
#@MusicAzBot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
 **🙋🏻‍♀️ Merhaba {}**
**👀 Benim İsmim [{}](https://t.me/{})   
🇦🇿 Ben Türk dilinde çok fonksiyonlu bir telegram botuyum.  
💁🏻‍♀️ Becerilerimi görmek için ardım düğmesine dokunun**   

"""    
    HELP_TEXT = """
 **🙋🏻‍♀️ Merhaba {}** 

 **💁🏻‍♀️ ️️️️️️ [{}](https://t.me/{})- in  
 📚 Yardım Komutları Bunlardır 
İstediğiniz Butonlara Dokunarak
 ✔️yardım ve bilgi alabilirsiniz** 
"""

    GSTART_TEXT = """
 **🙋🏻‍♀️ Merhaba {}**

 **💁🏻‍♀️ ️️️️️️ [{}](https://t.me/{})

 ❤️‍🔥 {}  Ben de grupta harika çalışıyorum  **
"""



### Bot Haqqında Ümumi Məlumat

    BH_TEXT = """

➻ **🙋🏻‍♀️ Merhaba {}**

➻ **👸🏻 [{}](https://t.me/{}) 🇦🇿 Türk dilinde çok fonsiyonlu botdur...**

➻ ✨ Bot Versiyonu: v0.7.0
➻ 🍀 Pyrogram Versiyonu: 1.4.16
➻ ✨ Python Versiyonu: 3.11.1
➻ ⚙️ Sunucu [Heroku](https://heroku.com)
➻ 📆 Bot Kullanıma verilen Tarihi `20.11.2022` 

╔═════════════════
║ **⚠️ Dikkat botun çalışması 
║➻ yönetici yetkilerinden sadece 
║➻ 💬 Mesajları Silme 🚫 Yetkisi Verin**
╚═════════════════
"""


    SAHIB_TEXT = """
╔═════════════════
║▻ 🔮 Kullanım: /stats
║▻ 📃 Açıklama: Bot hakkında genel bilgi sağlar.
║
║▻ 🔮 Kullanım: /block
║▻ 📃 Açıklama: Kullanıcıyı Veya Grubu Engeller.
║
║▻ 🔮 Kullanım: /unblock
║▻ 📃 Açıklama: Engellemeyi Kaldırır
║
║▻ 🔮 Kullanım: /blocklist
║▻ 📃 Açıklama: Engellenenlerin listesini gösterir.
║
║▻ 🔮 Kullanım: /broadcastall
║▻ 📃 Açıklama: Gruba ve Özele reklam yayın yapar.
║
║▻ 🔮 Kullanım: /gcast
║▻ 📃 Açıklama: Grublara reklam yayını yapar.
║
║▻ 🔮 Kullanım: /broadcast_pin
║▻ 📃 Açıklama: Grublara reklam yayınlar ve sabitleyer.
║
║▻ 🔮 Kullanım: /dyno
║▻ 📃 Açıklama: Heroku Dyno Tutarını Ölçür.
║
║▻ 🔮 Kullanım: /pin
║▻ 📃 Açıklama:  Yanıtlanan Mesajı sabitleyir.
╚═════════════════
"""

    MUSIC_TEXT = """
╔═════════════════
║▻ 🔮 Kullanım: /song 
║▻ 🧩 Örnek: /song Rei - Ah Canım Sevgilim
║▻ 📃 Açıklama: Muzik indirir.
║
║▻ 🔮 Kullanım: /video
║▻ 🧩 Örnek: /video Rei - Ah Canım Sevgilim
║▻ 📃 Açıklama: Video indirir.
║
║▻ 🔮 Kullanım: /lyrics 
║▻ 🧩 Örnek: /lyrics Rei - Ah Canım Sevgilim
║
║▻ 📃 Açıklama: Muzik sözlerini arar.
╚═════════════════
"""

    TELEGRAPH_TEXT = """
╔═════════════════
║▻ 🔮 Kullanım: /tgm
║▻ 📃 Açıklama: Fotoğraf, Video veya GIF göndererek bağlantı alabilirsiniz.
╚═════════════════
"""

    SEHID_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /sehid 
║▻ 📃 Açıqlama:  Bu əmr vaistəsiylə sizə **Şəhid** adları göndərəcəm
╚═════════════════
╔═════════════════
║▻ 🥀 **Allah bütün Şəhidimizə rəhmət eləsin**
║▻ 🤲 Qazilərimizə şəfa versin 
║▻ 😔 Başın sağolsun Azərbaycan 🇦🇿
║▻ 🇦🇿 Bazada **2881** Şəhid adı mövcuddur
╚═════════════════
""" 
    OYUN_TEXT = """
╔═════════════════
║▻ 🔮 Kullanım: /zer
║▻ 📃 Açıklama: zar atar
║
║▻ 🔮 Kullanım: /top
║▻ 📃 Açıklama: top atar
║
║▻ 🔮 Kullanım: /bowling
║▻ 📃 Açıklama: bowling atar
║
║▻ 🔮 Kullanım: /ox
║▻ 📃 Açıklama: yay atar
║
║▻ 🔮 Kullanım: /jackpot
║▻ 📃 Açıklama: jackpot atar
║
║▻ 🔮 Kullanım: /basket
║▻ 📃 Açıklama: basket atar
╚═════════════════
"""

    EYLENCE_TEXT = """
╔═════════════════
║▻ 🔮 Kullanım: /soxri 
║▻ 📃 Açıklama: Random 16+ Fotoğrafı Atar.
║
║▻ 🔮 Kullanım: /anime
║▻ 📃 Açıklama: Random Anime Fotoğrafı Atar
║
║▻ 🔮 Kullanım: /tema
║▻ 📃 Açıklama: Random Telegram Teması Atar
║
║▻ 🔮 Kullanım: /pp
║▻ 📃 Açıklama: Random Profil Fotoğrafı Atar
╚═════════════════
"""


    ELAVELER_TEXT = """
╔═════════════════
║▻ 🔮 Kullanım: /id
║▻ 📃 Açıklama: Kullanıcının kimliğini alın.
║
║▻ 🔮 Kullanım: /info
║▻ 📃 Açıklama: Kullanıcı hakkında bilgi sağlar
║
║▻ 🔮 Kullanım: /alive
║▻ 📃 Açıklama: Botun aktif olduğunu bildirir.
╚═════════════════
"""


    AXTARIS_TEXT = """
╔═════════════════
║▻ 🔮 Kullanım: /github 
║▻ 🧩 Örnek: /github Python
║▻ 📃 Açıklama: Github Araması Yapar.
║
║▻ 🔮 Kullanım: /search
║▻ 🧩 Örnek: /search Rei - Ah Canım Sevgilim
║▻ 📃 Açıklama: YouTube link arar.
╚═════════════════
"""

    TAGGER_TEXT = """
╔═════════════════
║▻ 🔮 Kullanım: /tag
║▻ 📃  Açıklama: [Sebep] - 5 - Li etiket.
║
║▻ 🔮 Kullanım: /ttag
║▻ 📃  Açıklama: [Sebep] - Tekli etiket.
║
║▻ 🔮 Kullanım: /etag
║▻ 📃  Açıklama: [Sebep] - Emoji ile etiket.
║
║▻ 🔮 Kullanım: /btag
║▻ 📃  Açıklama: [Sebep] - Bayraklarla etiket.
║
║▻ 🔮 Kullanım: /admin
║▻ 📃 Açıklama: Grub Yöneticilerin listesi.
╚═════════════════
"""



##### Broadcast Mesajları


class LAN(object):


    BILDIRIM = """**🆕 Yeni istifadəçi bota start etdi**\n\n👤 {}\n🆔 `{}`\n🔗 [{}](tg://user?id={})"""
    GRUP_BILDIRIM = """**🆕 Yeni istifdəçi bota qrupda start etdi**\n\n👤 Qrupa əlavə edən: `{}`\n🆔 Qrupa əlavə edən istifadəçi id: `{}`\n🔗 Profil linki: [{}](tg://user?id={})\nQrupun ID: {})

"""
    SAHIBIME = """
sahibimə
"""
    PRIVATE_BAN = """
Məyusam, əngəlləndiniz! Bunun bir xəta olduğunu düşünürsünüzsə {} yazın.
 """
    GROUP_BAN = """
Məyusam, qrupunuz qara siyahıya əlavə olundu! Artıq burada qala bilmərəm! Bunun bir xəta olduğunu düşünürsünüzsə {} yazın.'
"""
    NOT_ONLINE = """
aktiv deyil
"""
    BOT_BLOCKED = """
botu əngəlləyib
"""
    USER_ID_FALSE = """
istifadəçi ID yanlışdır.
"""
    BROADCAST_STARTED = """
```📥 Reklam yayımı başladı!\nBitəndə mesaj göndərəcəm
"""
    BROADCAST_STOPPED = """
```✅ Reklam yayımı uğurla tamamlandı.```\n\n**Bu qədər vaxtda tamamlandı** `{}`\n\n**Ümumi istifadəçilər:** `{}`\n\n**Ümumi göndərmə cəhdləri:** `{}`\n\n**Uğurla göndərilən:** `{}`\n\n**Ümumi xəta:** `{}`
"""
    STATS_STARTED = """
{} **Zəhmət olmasa gözləyin, bilgiləri gətirirəm!**
"""
    STATS = """
**@{} Məlumatları**\n\n**İstifadəçiləri;**\n» Ümumi: `{}`\n» Qruplar: `{}`\n» Şəxsi: `{}`\n\n**Disk İstifadəsi;**\n» Disk'in Sahəsi: `{}`\n» İstifadə Edilən: `{} ({}%)`\n» Boş Qalan: `{}`\n\n**🎛 Ən yüksək istifadə dəyərləri;**\n» CPU: `{}%`\n» RAM: `{}%`\n» Pyrogram: {}
"""
    BAN_REASON = """
Bu səbəbdən qadağan olundunuz @{} tərəfindən avtomatik olaraq yaradılmışdır."""
    NEED_USER = """
**Zəhmət olmasa istifadəçi ID'si yazın.**
"""
    BANNED_GROUP = """
🚷 **Qadağan olundu!\n\nQadağan edən:** {}\n**Qrup ID:** `{}`\n**Vaxt:** `{}`\n**Səbəb:** `{}`
"""
    AFTER_BAN_GROUP = """
**Məyusam, qrupunuz qara siyahıya əlavə edildi!\n\nSəbəb:** `{}`\n\n**Artıq burada qala bilmərəm. Bunun bir xəta olduğunu düşünürsünüzsə, dəstək qrupuna gəlin.**
"""
    GROUP_BILGILENDIRILDI = """\n\n✅ **Qrupu bilgiləndirdim və qrupdan çıxdım.**
"""
    GRUP_BILGILENDIRILEMEDI = """\n\n❌ **Qrupu məlumatlandırarkən xəta yarandı:**\n\n`{}`
"""
    USER_BANNED = """
🚷 **Qadağan olundu\n\nQadağan edən:** {}\n **İstifadəçi ID:** `{}`\n**Vaxt:** `{}`\n**Səbəb:** `{}`
"""
    AFTER_BAN_USER = """
**Məyusam, qara siyahıya əlavə edildiniz! \n\nSəbəb:** `{}`\n\n**Bundan sonra sizə xidmət etməyəcəyəm.**
"""
    KULLANICI_BILGILENDIRME = """\n\n✅ İstifadəçini məlumatlandırdım.
"""
    KULLANICI_BILGILENDIRMEME = """\n\n❌ **İstifadəçini məlumatlandırarkən xəta yarandı:**\n\n`{}`
"""
    UNBANNED_USER = """
🆓 **İstifadəçinin qadağası qaldırıldı!** \nQadağanı qaldıran: {}\n**İstifadəçi ID:** `{}`
"""
    USER_UNBAN_NOTIFY = """
🎊 Sizə gözəl bir xəbərim var! Artıq əngəliniz qaldırıldı!
"""
    BLOCKS = """
🆔 **İstifadəçi ID:** `{}`\n⏱ **Vaxt:** `{}`\n🗓 **Qadağan edildiyi tarix:** `{}`\n💬 **Səbəb:** `{}`\n\n"""
    TOTAL_BLOCK = """
🚷 **Ümumi əngəllənən:** `{}`\n\n{}
"""
