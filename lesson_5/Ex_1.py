def gen_odd_nums(max_nums):
    for num in range(1, max_nums + 1, 2):
        yield num


odd_to_number = gen_odd_nums(15)
"""Добавим в цикл лишнюю итерацию, что бы увидеть: StopIteration"""
for i in range(1, 18, 2):
    print(next(odd_to_number))
