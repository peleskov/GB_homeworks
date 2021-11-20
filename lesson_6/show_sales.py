import sys


def show_sales(interval):
    f = open('shop/bakery.csv', 'r', encoding='utf-8')
    sales = ''
    if len(interval) > 0:
        if len(interval) == 1:
            interval.append(len([0 for _ in f]))
            f.seek(0)
        for i in range(0, int(interval[1])):
            line = f.readline()
            if i >= int(interval[0]) - 1:
                sales = sales + line
    else:
        sales = f.read()
    f.close()
    return sales.strip()


print(show_sales(sys.argv[1:3]))
