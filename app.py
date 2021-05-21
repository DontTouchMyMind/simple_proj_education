from aiogram import executor, types

# from utils.notify_admins import on_startup_notify
from handlers import dp


#
# async def on_startup(dispatcher):
#     await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp)
