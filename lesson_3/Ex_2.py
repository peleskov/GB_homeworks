DICTIONARY = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(num):
    return DICTIONARY.get(num.lower()).capitalize() if num[0].isupper() else DICTIONARY.get(num.lower())


print(num_translate('one'))
print(num_translate("Eight"))
print(num_translate("ten1"))
