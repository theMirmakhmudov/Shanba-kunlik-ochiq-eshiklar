from aiogram import types
from buttons import button
from db import Database

db = Database("database.db")


async def start(message: types.Message):
    if message.from_user.id == 6543698942:
        await message.answer(f"Assalomu Aleykum.Xurmatli Admin", reply_markup=button)
    else:
        await message.answer(f"Assalomu Aleykum.Xurmatli {message.from_user.full_name}")
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.full_name, message.from_user.username, message.from_user.id)
        else:
            await message.answer("siz avval ham botga start boshgansiz")
