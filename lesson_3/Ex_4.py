from pprint import pprint


def dictionary_sort(dictionary):
    result = {}
    for k in sorted(dictionary.keys()):
        if type(dictionary[k]) is dict:
            result[k] = dictionary_sort(dictionary[k])
        elif type(dictionary[k]) is list:
            result[k] = sorted(dictionary[k])
        else:
            result[k] = dictionary[k]
    return result


def thesaurus_adv(*full_names):
    dictionary = {}
    for fullname in full_names:
        fullname = fullname.title()
        key_last_name = fullname.split()[1][0]
        key_first_name = fullname.split()[0][0]
        if key_last_name not in dictionary:
            dictionary.update({key_last_name: {key_first_name: [fullname]}})
        elif key_first_name not in dictionary[key_last_name]:
            dictionary[key_last_name].update({key_first_name: [fullname]})
        else:
            dictionary[key_last_name][key_first_name].append(fullname)
    return dictionary_sort(dictionary)


out = thesaurus_adv("Станислав ярушин", "михаил яковлев", "Инна Серова", "иван сергеев", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(out, '\n')
pprint(out)
