from telegram import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🔥 Mahsulotlar", web_app=WebAppInfo("https://google.com")
            ),
            KeyboardButton(text="📥Savat"),
        ],
        [KeyboardButton(text="💼 Hamkorlik"), KeyboardButton(text="ℹ️ Ma'lumot")],
        [KeyboardButton(text="🌐 Tilni tanlash")],
    ]
)

info_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✍️ Izoh qoldirish")],
        [
            KeyboardButton(text="🚀 Yetkazib berish shartlari"),
            KeyboardButton(text="☎️ Kontaktlar"),
        ],
        [KeyboardButton(text="🏠 Bosh menyu")],
    ]
)

comments_keyboard = ReplyKeyboardMarkup(keyboard=[[]])

lang_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="uzbekcha", callback_data="lang:uz")],
        [InlineKeyboardButton(text="ruscha", callback_data="lang:ru")],
    ]
)
