from AylinRobot.config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
  
### START BUTTONU 

START_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('👾 Resmi Kanal', url=f"https://t.me/{Config.CHANNEL}")
InlineKeyboardButton("💬 Destek Grubu", url=f"https://t.me/{Config.SUPPORT}")
],[
InlineKeyboardButton('ℹ️ Bot Hakkında', callback_data='bh'),  
InlineKeyboardButton('📚  Yardım', callback_data='help'),
],[        
InlineKeyboardButton('➕ Beni Gruba Ekle ➕', url=f"https://t.me/{Config.BOT_USERNAME}?startgroup=true"),
],[                
InlineKeyboardButton('👨‍💻 Sahib',  url=f"https://t.me/{Config.OWNER_NAME}"),
]]
#### KÖMƏK BUTTONU

HELP_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🎧 Muzik', callback_data='musıc'),
InlineKeyboardButton('⭐ Telegram', callback_data='tg')
],[
InlineKeyboardButton('🎮 Oyunlar', callback_data='oyun'),        
InlineKeyboardButton('🌀 Eğlence', callback_data='eylence'),
],[
InlineKeyboardButton('♾️ Takviyeler', callback_data='elave'),
InlineKeyboardButton('🔍 Arama', callback_data='axtar'),
],[
InlineKeyboardButton('🛎 Etiket', callback_data='tag'),    
InlineKeyboardButton('👨‍💻 Sahip Komutları', callback_data='sahib'),
],[    
InlineKeyboardButton('🔐 Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri', callback_data='home'),]])

### GERİ BUTTONU    

MUSIC_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri', callback_data='help'),]])
TELEGRAPH_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri', callback_data='help'),]])
SEHID_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri', callback_data='help'),]])        
OYUN_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri', callback_data='help'),]])
EYLENCE_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri', callback_data='help'),]])     
SAHIB_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri', callback_data='help'),]])
ELAVE_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri', callback_data='help'),]])
AXTAR_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri', callback_data='help'),]])
TAGGER_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri', callback_data='help'),]])
BH_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Kapat', callback_data='close'),   
InlineKeyboardButton('🔙 Geri', callback_data='home'),]])
GS_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Kapat', callback_data='close'),]])   
