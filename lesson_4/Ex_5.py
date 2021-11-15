from utils import currency_rates
import sys


if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        print(currency_rates(sys.argv[i]))
else:
    print('Не указаны валюты!')
