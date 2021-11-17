from itertools import zip_longest


def gen_assign1(tutors, classes):
    for el in list(zip(tutors, classes)):
        yield el


def gen_assign2(tutors, classes):
    for el in list(zip_longest(tutors, classes)):
        yield el


list_tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
list_classes = [
    '9А', '7В', '9Б', '9В',
    '8Б', '10А', '10Б', '9А'
]

result = gen_assign1(list_tutors, list_classes)
print(type(result))
for i in range(1, min(len(list_tutors), len(list_classes)) + 1):
    print(next(result))

result = gen_assign2(list_tutors, list_classes[:-2])
print(type(result))
for i in range(1, max(len(list_tutors), len(list_classes[:-2])) + 1):
    print(next(result))
