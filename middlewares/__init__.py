from .big_brothers import BigBrother

from loader import dp


if __name__ == '__main__':
    dp.middleware.setup(BigBrother())