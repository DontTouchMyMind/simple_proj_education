from .big_brothers import BigBrother

from loader import dp


if __name__ == 'middlewares':
    dp.middleware.setup(BigBrother())   # Можно установить в app.py -> main
