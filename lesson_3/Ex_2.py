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
    translate = num_dictionary[num.lower()] if num.lower() in num_dictionary else None
    return translate.title() if translate is not None and num.istitle() else translate


print(num_translate('One'))
print(num_translate('two'))
print(num_translate("ten1"))
