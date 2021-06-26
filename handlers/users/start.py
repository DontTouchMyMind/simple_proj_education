import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from filters import SomeFilter
from loader import dp, bot
from utils.misc.throttling import rate_limit


@rate_limit(5, key='start')
@dp.message_handler(CommandStart(), SomeFilter())
async def bot_start(message: types.Message, middleware_data, filter_data):
    await message.answer(f"Hello, {message.from_user.full_name}!\n{middleware_data=}\n{filter_data}",
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text='The simple button', callback_data='button')
                                 ]
                             ]
                         ))


@dp.callback_query_handler(text='button')
async def get_button(call: types.CallbackQuery):
    await call.message.answer("U pressed the button")

# DEPRECATED ()
# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     non_existing_user = 666666
#
#     # Не попадает в эррор хендер, обрабатывается тут с помощью try
#     try:
#         await message.answer("Неправильно закрыт <b>тег<b>")
#     except Exception as err:
#         await message.answer(f"Не попало в эррор хендлер. Ошибка: {err}")
#
#     # Не попадает в эррор хендер
#     try:
#         await bot.send_message(chat_id=non_existing_user, text="Не существующий пользователь")
#     except Exception as err:
#         await message.answer(f"Не попало в эррор хендлер. Ошибка: {err}")
#
#     # Попадает отсюда в эррор хендлер
#     await message.answer("Не существует <kek>тега</kek>")
#     logging.info("Это не выполнится, но бот не упадет.")
#
#     # Все что ниже - не выполнится, но бот не упадет
#
#     await message.answer("...")