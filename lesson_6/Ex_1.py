import requests

with open('in_data/nginx.log', 'w+', encoding='utf-8') as f:
    nginx_log = requests.get(
        'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
    f.write(nginx_log.text)
    f.seek(0)
    result = list((line.split()[0], line.split()[5].strip('"'), line.split()[6]) for line in f)

print(result)
