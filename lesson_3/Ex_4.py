from pprint import pprint
from Ex_3 import dictionary_sort


def thesaurus_adv(*full_names):
    dictionary = {}
    for fullname in full_names:
        fullname = fullname.title()
        fullname_split = fullname.split()
        key_last_name = fullname_split[1][0]
        key_first_name = fullname_split[0][0]
        dictionary.setdefault(key_last_name, {})
        dictionary[key_last_name].setdefault(key_first_name, [])
        dictionary[key_last_name][key_first_name].append(fullname)
    return dictionary_sort(dictionary)


out = thesaurus_adv("Станислав ярушин", "михаил яковлев", "Инна Серова", "иван сергеев", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(out, '\n')
pprint(out)
