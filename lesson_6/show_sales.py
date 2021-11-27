import sys

with open('shop/bakery.csv', 'r', encoding='utf-8') as f:
    interval = sys.argv[1:3]
    if len(interval) > 0:
        if len(interval) == 1:
            interval.append(sum(1 for _ in f))
        f.seek(0)
        for i in range(0, int(interval[1])):
            line = f.readline()
            if i >= int(interval[0]) - 1:
                print(line.strip())
    else:
        for line in f:
            print(line.strip())
