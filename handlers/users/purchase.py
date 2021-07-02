import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keybords.inline.callback_datas import buy_callback
from keybords.inline.choice_buttons import choice
from loader import dp, bot


@dp.message_handler(Command('item'))
async def show_items(message: types.Message):
    await message.answer(
        text=f"There are two products for sale: 5 apples and 1 pear.\n"
             f"If you don't need anything click cancel.",
        reply_markup=choice
    )


# Отлавливаем нажатие кнопки Купи Грушу
@dp.message_handler(buy_callback.filter(item_name='pear'))
async def buying_pear(call: CallbackQuery, callback_data: dict):    # callback_data - создается фильтром buy_callback.filter
    # await bot.answer_callback_query(callback_query_id=call.id)     # Закрываем часики!
    # Или так
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data DICT = {callback_data}")
