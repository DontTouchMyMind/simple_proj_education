import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import banned_users


# В этом мидлваре можно делать запрос к базе данных, напр. достать список заблокированных юзеров
class BigBrother(BaseMiddleware):
    # 1
    # on_<point>_<event_type>
    async def on_pre_process_update(self, update: types.Update, data: dict):

        logging.info("[------------New update-------------]")
        logging.info("1.Pre Process Update")
        data['PPU'] = "It's some data was added in PreProcessUpdate"
        print(data)
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

    # 2
    async def on_process_update(self, update: types.Update, data: dict):
        logging.info("2. Process Update")
        logging.info(f"Data from Pre Process Message {data}")
        data['PU'] = "It's some data was added in ProcessUpdate"
        logging.info(f"Update = {update}")
        logging.info("The next step is PreProcessMessage")

    # 3
    async def on_pre_process_message(self, message: types.Message, data: dict):
        logging.info("3.Pre Process Message")
        logging.info(f"Input data = {data}")
        logging.info("The next step is Filters -> ProcessMessage")
        data['PPM'] = "It's some data was added in PreProcessMessage"

    # 4 Filters

    # 5
    async def on_process_message(self, message: types.Message, data: dict):
        logging.info("5. Process Message")
        logging.info(f"Input data = {data}")
        logging.info("The next step is Filters -> ProcessMessage")
        data['PM'] = "It's some data was added in ProcessMessage"
        print(f"data from PM = {data}")
        new_data = {
            'PM': data.get('PM'),
            'PPM': data.get('PPM')
        }
        data['middleware_data'] = new_data
        # Data from PM mb send to events handler
        # data from PM = {
        #   'PPM': "It's some data was added in PreProcessMessage",
        #   'state': < aiogram.dispatcher.storage.FSMContext object at 0x7fc9b10d7790 >,
        #   'raw_state': None,
        #   'PM': "It's some data was added in ProcessMessage"}
