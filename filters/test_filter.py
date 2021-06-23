import logging

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import ctx_data


class SomeFilter(BoundFilter):
    async def check(self, message: types.Message):
        # Take data from context
        data = ctx_data.get()

        logging.info(f"#4. Filters, {data=}")
        logging.info("The next step is Process Message")

        return {
            'filter_data': 'This data from filter!',
            'PPM': data.get('PPM')
        }
        # return {'filter_data': data.get('PPM')}
