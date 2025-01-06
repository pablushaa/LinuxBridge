from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = [
    [InlineKeyboardButton(text="🔄 Перезагрузка", callback_data="reboot"),
    InlineKeyboardButton(text="⚙️ Выполнить команду", callback_data="run")],
    [InlineKeyboardButton(text="🖼️ Скриншот", callback_data="screen")]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)

kb = [[KeyboardButton(text="🏚 Главное меню"), KeyboardButton(text="❔ О боте")]]
kb = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)