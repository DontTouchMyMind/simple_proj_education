from aiogram import types

from loader import dp


@dp.message_handler(content_types='text', state=None)
async def bot_echo(message: types.Message):
    chat_id = message.chat.id
    text = message.text
    print(text)
    await dp.bot.send_message(chat_id=chat_id, text=text)

    await message.answer(f'{text} from answer alice')
    await message.reply(f'{text} from reply alice')
