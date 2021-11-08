price_list = [41, 88.8, .5, .08, 97.98, 25.08, 96.28, 59.99, 65.74, 83.66]


def make_string(list):
    result_list = []
    for price in list:
        price_split = f'{price:.2f}'.split('.')
        result_list.append(f'{price_split[0]} руб {price_split[1]} коп')
    return ', '.join(result_list)


# Ex. A
print(make_string(price_list), '\n')

# Ex. B
print(f'Original price_list id: {id(price_list)}')
price_list.sort()
print(f'Sorted increase price_list id: {id(price_list)}')
print(make_string(price_list), '\n')

# Ex. C
new_price_list = price_list.copy()  # new_price_list = price_list[:]
new_price_list.sort(reverse=True)
print(f'Original price_list id: {id(price_list)}')
print(make_string(price_list))
print(f'Sorted decrease price_list id: {id(new_price_list)}')
print(make_string(new_price_list), '\n')

# Ex. D
print(make_string(price_list[-5:]))
