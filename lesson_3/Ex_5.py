import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "вечером"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "красный", "темный"]


def get_jokes(qty: int = 1, repeat: bool = True):
    """
    Making a list of jokes
    :param qty: quantity of jokes
    :param repeat: repeat words in jokes
    :return: list of jokes
    """
    out = []
    if repeat:
        for i in range(qty):
            out.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    else:
        random.shuffle(nouns)
        random.shuffle(adverbs)
        random.shuffle(adjectives)
        for i in range(min([qty, len(nouns), len(adverbs), len(adjectives)])):
            out.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')
    return out


print(get_jokes(6))
print(get_jokes(10, False))
