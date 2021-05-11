from aiogram import executor, types

# from utils.notify_admins import on_startup_notify
from loader import dp, bot


#
# async def on_startup(dispatcher):
#     await on_startup_notify(dispatcher)

@dp.message_handler(content_types='text', state=None)
async def bot_echo(message: types.Message):
    chat_id = message.chat.id
    text = message.text
    print(text)
    await bot.send_message(chat_id=chat_id, text=text)

    await message.answer(f'{text} from answer alice')
    await message.reply(f'{text} from reply alice')

if __name__ == '__main__':
    executor.start_polling(dp)
