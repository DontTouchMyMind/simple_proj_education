from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keybords.inline.callback_datas import buy_callback

# choice = InlineKeyboardMarkup(
#     row_width=2,
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(
#                 text="Купи грушу",
#                 callback_data=buy_callback.new(
#                     item_name='pear',
#                     quantity=1
#                 )
#                 # callback_data="buy:pear:1"
#             ),
#             InlineKeyboardButton(
#                 text="Купи яблоки",
#                 callback_data="buy:apple:5"    # Расшифровка buy_callback.new()
#             ),
#             InlineKeyboardButton(
#                 text="Отмена",
#                 callback_data="cancel"
#             )
#         ]
#     ]
# )

# Вариант 2 - с помощью row_width и insert.
choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="Купить грушу", callback_data=buy_callback.new(item_name="pear", quantity=1))
choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="Купить яблоки", callback_data="buy:apple:5")
choice.insert(buy_apples)

cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
choice.insert(cancel_button)

pear_keyboard = InlineKeyboardMarkup()
pear_link = InlineKeyboardButton(text="Buy here!", url="https://www.google.com/search?q=pear")
pear_keyboard.insert(pear_link)

apples_keyboard = InlineKeyboardMarkup()
apple_link = InlineKeyboardButton(text="Buy here!", url="https://www.google.com/search?q=apple")
apples_keyboard.insert(apple_link)
# Another way to create a keyboard

# pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(text="Купи тут", url="https://www.google.com/search?q=pear")
#     ]
# ])
# apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(text="Купи тут", url="https://www.google.com/search?q=apple")
#     ]
# ])
