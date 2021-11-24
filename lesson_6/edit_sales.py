import sys
import os

edit_info = sys.argv[1:3]
with open('shop/bakery.csv', 'r', encoding='utf-8') as f:
    with open('shop/bakery_tmp.csv', 'w', encoding='utf-8') as tmp:
        length_f = sum(1 for _ in f)
        f.seek(0)
        if len(edit_info) != 2 or int(edit_info[0]) > length_f:
            print('Нет такой записи!')
            exit()
        else:
            for i in range(1, length_f + 1):
                line = f.readline()
                if i == int(edit_info[0]):
                    tmp.write(f'{edit_info[1]}\n')
                else:
                    tmp.write(line)

os.remove('shop/bakery.csv')
os.rename('shop/bakery_tmp.csv', 'shop/bakery.csv')
print('Цена изменена!')
