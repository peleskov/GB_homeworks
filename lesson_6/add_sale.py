import sys

if len(sys.argv) < 2:
    print('Укажите продажи через пробел')
else:
    sales = '\n'.join([f'{sale}' for sale in sys.argv[1:]])
    with open('shop/bakery.csv', 'a+', encoding='utf-8') as f:
        f.write(f'{sales}\n')
    print('Продажи добавлены!')
