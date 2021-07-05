import logging

from aiogram import types
from aiogram.dispatcher.filters import Command

from keybords.inline.callback_datas import buy_callback
from keybords.inline.choice_buttons import choice, pear_keyboard, apples_keyboard
from loader import dp, bot


@dp.message_handler(Command("items"))
async def show_items(message: types.Message):
    await message.answer(
        text=f"There are two products for sale: 5 apples and 1 pear.\n"
             f"If you don't need anything click cancel.",
        reply_markup=choice
    )


# Отлавливаем нажатие кнопки Купи Грушу
@dp.callback_query_handler(text_contains="pear")
async def buying_pear(call: types.CallbackQuery):    # callback_data - создается фильтром buy_callback.filter
    # await bot.answer_callback_query(callback_query_id=call.id)     # Закрываем часики!
    # Или так
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data DICT = {callback_data}")
    # quantity = callback_data.get('quantity')
    await call.message.answer(f"You have chosen to buy a pear. Pears in total 1. Thx!",
                              reply_markup=pear_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name="apple"))
async def buying_apple(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"{callback_data=}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"You have chosen to buy apples. Apples in total {quantity}. thx!",
                              reply_markup=apples_keyboard)


@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: types.CallbackQuery):
    await call.answer("You have canceled this purchase!", show_alert=True)

    # 1.Отправляем пустую клваиатуру изменяя сообщение, для того, чтобы ее убрать из сообщения!
    await call.message.edit_reply_markup(reply_markup=None)

    # 2. Отправляем пустую клваиатуру (по API)
    # await bot.edit_message_reply_markup(chat_id=call.from_user.id,
    #                                     message_id=call.message.message_id,
    #                                     reply_markup=None)