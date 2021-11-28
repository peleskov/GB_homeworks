import requests
import re
import os

if not os.path.isfile('nginx_logs.txt'):
    with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
        logs = requests.get(
            'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
        f.write(logs.text)

result = []
pattern = r'(?P<ip>-?^([\da-z]+[:.]{1,})+[\da-z]+)(\s-){2,}\s\['
pattern += r'(?P<date>-?[\d]{2}\/[A-Za-z]+\/[\d]{4}(:[\d]{2}){3}\s\+[\d]{4})\]\s\"'
pattern += r'(?P<type>-?[A-Z]{3,4})\s'
pattern += r'(?P<resource>-?[\w\/\.]+)\sHTTP\/1.1"\s'
pattern += r'(?P<code>-?[\d]+)\s'
pattern += r'(?P<size>-?[\d]+)\s'
parser = re.compile(pattern)

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        res = parser.match(line)
        try:
            result.append((res.group('ip'), res.group('date'), res.group('type'), res.group('resource'),
                           res.group('code'), res.group('size')))
        except Exception as e:
            '''Поиск не стандартных строк'''
            print(line, e)

print(result)
