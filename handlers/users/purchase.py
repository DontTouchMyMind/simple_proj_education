from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('item'))
async def show_items(message: types.Message):
    await message.answer(
        text=f"There are two products for sale: 5 apples and 1 pear.\n"
             f"If you don't need anything click cancel.",
        reply_markup=choice
    )