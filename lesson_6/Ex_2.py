with open('in_data/nginx.log') as f:
    result = list((line.split()[0], line.split()[5].strip('"'), line.split()[6]) for line in f)

result_ips = {}
for item in result:
    result_ips.setdefault(item[0], 0)
    result_ips[item[0]] += 1

req_count = {item: result_ips[item]
             for item in sorted(result_ips, key=result_ips.get, reverse=True)
             if result_ips[item] > 1000}
print('spammers: ', req_count)
