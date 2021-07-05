from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keybords.default import menu
from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    """The calling to keyboard 'Menu'."""
    await message.answer("Check entity from the next menu", reply_markup=menu)


@dp.message_handler(text='Meats')
async def get_meats(message: types.Message):
    """The handling of click button 'Meats'."""
    await message.answer("Your choice is MEATS")


@dp.message_handler(Text(equals=['Corn', 'Potato']))
async def get_vegetables(message: types.Message):
    """The handling of click the several buttons."""
    await message.answer(f"Your choice is {message.text}", reply_markup=ReplyKeyboardRemove())