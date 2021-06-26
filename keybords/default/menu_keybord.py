from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Meats')
        ],
        [
            KeyboardButton(text='Corn'),
            KeyboardButton(text='Potato')
        ],
    ],
    resize_keyboard=True
)