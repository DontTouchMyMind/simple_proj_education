from loader import dp
from .test_filter import SomeFilter

if __name__ == 'filters':
    dp.filters_factory.bind(SomeFilter)