import requests
import xml.etree.ElementTree as ET
from decimal import Decimal
from datetime import datetime

def currency_rates(currency):
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if r.status_code != 200:
        return 'Server not responding!'
    else:
        root = ET.fromstring(r.text)
        currency_date = datetime.strftime(datetime.strptime(root.get('Date'), '%d.%m.%Y'), '%d/%m/%Y')
        currency_info = root.find(f"Valute[CharCode='{currency.upper()}']")
        if currency_info:
            return f"Курс на {currency_date} {currency_info.find('Name').text}: {currency_info.find('Nominal').text} {currency_info.find('CharCode').text} = {Decimal(currency_info.find('Value').text.replace(',','.'))} руб"


print(currency_rates('usd'))
print(currency_rates('Eur'))
print(currency_rates('Aud'))
print(currency_rates('Auds'))
print(currency_rates(''))
