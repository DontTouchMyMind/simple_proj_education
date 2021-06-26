from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from utils.db_api.models import User
from utils.misc.sentinel import allow_access


@allow_access()
@dp.message_handler(Command('block_me'))
async def block_me(message: types.Message, user: User):
    await message.answer(f"User has status is {user.allowed}. And now access denied!\n"
                         f"Use /unblock_me command for unblocking!")
    user.block()


@allow_access()
@dp.message_handler(Command('unblock_me'))
async def unblock_me(message: types.Message, user: User):
    await message.answer(f"User has status is {user.allowed}. And now access successful!\n"
                         f"Use /block_me command for blocking!")
    user.allow()
