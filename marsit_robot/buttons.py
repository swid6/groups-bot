from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

bosh_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👨‍👩‍👦 Я родител", callback_data="Ota ona"),
            InlineKeyboardButton(text="👨‍🎓 Я студент", callback_data="O'quvchi"),
            InlineKeyboardButton(text="👤 Я гость", callback_data="Mehmon")
        ]
    ]
)

ota_ona_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏫 О школе"),
            KeyboardButton(text="👨‍👩‍👦 Добавыть ребенка")
        ]
    ],
    resize_keyboard=True
)

oquvchi_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍 Филиалы"),
            KeyboardButton(text="📝 О нашых курсах"),
            KeyboardButton(text="🔥 Работы наших учеников")
        ],
        [
            KeyboardButton(text="⭐️ Отзывы"),
            KeyboardButton(text="☎️ Контакты и наши страницы"),
            KeyboardButton(text="🏫 О школе")
        ],
        [
            KeyboardButton(text="✍️ Оставыт отзыв")  
        ]
    ],
    resize_keyboard=True
)

location_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="ТИНЧЛИК", callback_data="tinchlik"),
            InlineKeyboardButton(text="ЮНУСАБАД", callback_data="yunusobod")
        ]
    ]
)