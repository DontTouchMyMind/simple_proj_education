from loader import dp

from .big_brothers import BigBrother
from .throttling import ThrottlingMiddleware
from .acl import ACLMiddleware
from .sentinel import Sentinel


if __name__ == 'middlewares':
    # ORDER is important!
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(ACLMiddleware())
    dp.middleware.setup(Sentinel())
    dp.middleware.setup(BigBrother())   # Можно установить в app.py -> main
