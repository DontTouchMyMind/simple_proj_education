from aiogram import types

from loader import dp


@dp.message_handler(content_types='text', state=None)
async def bot_echo(message: types.Message, middleware_data):
    chat_id = message.chat.id
    text = message.text
    print(text)
    await dp.bot.send_message(chat_id=chat_id, text=text)

    await message.answer(f'{text} from answer alice')
    await message.reply(f'{text} from reply alice')
    print(f"Middleware data = {middleware_data}")
    await message.answer(f"From middleware date {middleware_data}")