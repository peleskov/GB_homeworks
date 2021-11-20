import requests

result = []
with open('in_data/nginx.log', 'w+') as f:
    nginx_logs = requests.get(
        'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
    f.write(nginx_logs.text)
    f.seek(0)
    while True:
        line = f.readline()
        if not line:
            break
        result.append((line.split()[0], line.split()[5].strip('"'), line.split()[6]))
print(result)
