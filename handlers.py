from aiogram import types
from buttons import button


async def start(message: types.Message):
    if message.from_user.id == 6543698942:
        await message.answer(f"Assalomu Aleykum.Xurmatli Admin", reply_markup=button)
    else:
        await message.answer(f"Assalomu Aleykum.Xurmatli {message.from_user.full_name}")
