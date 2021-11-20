result = []
with open('in_data/nginx.log', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        result.append((line.split()[0], line.split()[5].strip('"'), line.split()[6]))

result_ip = [item[0] for item in result]
req_count = [(ip, result_ip.count(ip)) for ip in set(result_ip)]
req_count_sorted = [item for item in sorted(req_count, key=lambda x: x[1], reverse=True) if item[1] > 1000]
spammer = max(req_count_sorted, key=lambda x: x[1])
print('suspect: ', req_count_sorted)
print('spammer: ', spammer)
