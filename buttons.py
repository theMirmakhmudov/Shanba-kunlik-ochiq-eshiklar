from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

btn = [
    [KeyboardButton(text="Chat"), KeyboardButton(text="Users")]
]

button = ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True)
