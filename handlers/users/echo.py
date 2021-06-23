import logging

from aiogram import types

from filters import SomeFilter
from loader import dp


@dp.message_handler(SomeFilter(), content_types='text', state=None)
async def bot_echo(message: types.Message, middleware_data, filter_data, PPM):
    chat_id = message.chat.id
    text = message.text
    print(text)
    await dp.bot.send_message(chat_id=chat_id, text=text)

    await message.answer(f'{text} from answer alice')
    await message.reply(f'{text} from reply alice')
    print(f"Middleware data = {middleware_data}")
    print(f"Filter data = {filter_data}")
    await message.answer(f"From middleware date {middleware_data} \n {filter_data=} \n {PPM=}")
    logging.info('6. Handler')
    logging.info('The next step is Post Process Message')

    return {'handler_data': 'The data from handler'}