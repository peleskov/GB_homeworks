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


def thesaurus(*names_tuple):
    dictionary = {}
    for name in names_tuple:
        name = name.title()
        key = name[0]
        dictionary[key].append(name) if key in dictionary else dictionary.update({key: [name]})
    return dictionary_sort(dictionary)


print(thesaurus("Станислав", "Мария", "семён", "Иван", "Петр", "илья", "сергей"))
