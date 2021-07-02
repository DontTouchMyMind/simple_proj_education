from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keybords.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Купи грушу',
                callback_data=buy_callback.new(
                    item_name='pear',
                    quantity=1
                )
            ),
            InlineKeyboardButton(
                text='Купи яблоки',
                callback_data='buy:apple:5'     # Расшифровка buy_callback.new()
            ),
            InlineKeyboardButton(
                text='Отмена',
                callback_data='cancel'
            )
        ]
    ]
)
# Another way to create a keyboard
pear_keyboard = InlineKeyboardMarkup()

PEAR_LINK = 'https://www.google.com/search?q=pear'

pear_link = InlineKeyboardButton(text='Buy here', link=PEAR_LINK)

pear_keyboard.insert(pear_link)
