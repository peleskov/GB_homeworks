import re

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for item in my_list[:]:
    index = my_list.index(item)
    if item.isdigit():
        my_list[index] = f'{int(item):02d}'
        my_list.insert(index, '"')
        my_list.insert(index+2, '"')
    elif item[0] in ('+', '-') and item[1:].isdigit():
        my_list[index] = f'{item[0]}{int(item[1:]):02d}'
        my_list.insert(index, '"')
        my_list.insert(index + 2, '"')

print(my_list)
print(re.sub(r'" ([-+]?\d+) "', r'"\1"', ' '.join(my_list)))
