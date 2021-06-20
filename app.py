from aiogram import executor

import middlewares, filters, handlers   # Порядок импортов важен!
from loader import dp
from middlewares import BigBrother

from utils.notify_admins import on_startup_notify


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    dp.middleware.setup(BigBrother())
    executor.start_polling(dp, on_startup=on_startup)
