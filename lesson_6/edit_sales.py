import sys
import os


def edit_sale(edit_info):
    with open('shop/bakery.csv', 'r', encoding='utf-8') as f, open('shop/bakery_tmp.csv', 'w', encoding='utf-8') as tmp:
        length_f = len([0 for _ in f])
        f.seek(0)
        if len(edit_info) == 0 or int(edit_info[0]) > length_f:
            return 'Нет такой записи!'
        for i in range(1, length_f + 1):
            line = f.readline()
            if i == int(edit_info[0]):
                tmp.write(f'{edit_info[1]}\n')
            else:
                tmp.write(line)
    os.remove('shop/bakery.csv')
    os.rename('shop/bakery_tmp.csv', 'shop/bakery.csv')
    return 'Цена изменена!'


print(edit_sale(sys.argv[1:3]))
