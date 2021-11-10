def num_translate(num):
    num_dictionary = {
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
    return num_dictionary[num.lower()] if num.lower() in num_dictionary else None


print(num_translate('one'))
print(num_translate("Eight"))
print(num_translate("ten1"))
