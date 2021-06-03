from loader import dp
from .big_brothers import BigBrother


if __name__ == '__main__':
    dp.middleware.setup(BigBrother())