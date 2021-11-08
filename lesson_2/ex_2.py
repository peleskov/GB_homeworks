import re

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

my_new_list = []
for item in my_list:
    if item.isdigit():
        my_new_list.extend(['"', f'{int(item):02d}', '"'])
    elif item[0] in ('+', '-') and item[1:].isdigit():
        my_new_list.extend(['"', f'{item[0]}{int(item[1:]):02d}', '"'])
    else:
        my_new_list.append(item)

print(my_new_list)

# Вариант 1
result = ''
separator = ' '
for item in my_new_list:
    if item == '"':
        separator = '' if separator == ' ' else ' '
    result += f'{item}{separator}'

print(result.rstrip())


# Вариант 2
print(re.sub(r'" ([-+]?\d+) "', r'"\1"', ' '.join(my_new_list)))
