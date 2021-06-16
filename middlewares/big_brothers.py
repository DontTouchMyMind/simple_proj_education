import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import banned_users


# В этом мидлваре можно делать запрос к базе данных, напр. достать список заблокированных юзеров
class BigBrother(BaseMiddleware):
    # on_point_event_type
    async def on_pre_process_update(self, update: types.Update, data: dict):
        print('ppu')
        logging.info("[------------New update-------------]")
        logging.info("1.Pre Process Update")
        data['PPU'] = "It's some data was added in PreProcessUpdate"
        logging.info(f"Update = {update}")
        logging.info("The next step is ProcessUpdate")

        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return

        if user in banned_users:
            raise CancelHandler()

    async def on_process_update(self, update: types.Update, data: dict):
        logging.info("2. Process Update")
        logging.info(f"Data from Pre Process Message {data}")
        data['PU'] = "It's some data was added in ProcessUpdate"
        logging.info(f"Update = {update}")
        logging.info("The next step is PreProcessMessage")

    async def on_pre_process_message(self, message: types.Message, data: dict):
        logging.info("3.Pre Process Message")
        logging.info(f"Input data = {data}")
        logging.info("The next step is Filters -> ProcessMessage")
        data['PPM'] = "It's some data was added in PreProcessMessage"
