import random


def get_jokes(qty: int = 1, repeat: bool = True):
    """
    Making a list of jokes
    :param qty: quantity of jokes
    :param repeat: repeat words in jokes
    :return: list of jokes
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "вечером"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "красный", "темный"]
    out = []
    if repeat:
        for i in range(qty):
            out.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    else:
        for i in range(min([qty, len(nouns), len(adverbs), len(adjectives)])):
            out.append(f'{nouns.pop(random.randint(0, len(nouns)-1))} {adverbs.pop(random.randint(0, len(adverbs)-1))} {adjectives.pop(random.randint(0, len(adjectives)-1))}')
    return out


print(get_jokes(6))
print(get_jokes(10, False))
