def calc_sum(numbers, increment=0):
    result = 0
    for number in numbers:
        num = number + increment
        sum_digits = 0
        for digit in list(str(num)):
            sum_digits += int(digit)
        result += num if sum_digits % 7 == 0 else 0
    return result


# вариант 1
numbers_1 = [num ** 3 for num in range(1, 1001, 2)]
print(calc_sum(numbers_1))
numbers_2 = [num ** 3 + 17 for num in range(1, 1001, 2)]
print(calc_sum(numbers_2))
print(calc_sum(numbers_1, 17))


# вариант 2
print(sum([number for number in numbers_1 if sum([int(i) for i in list(str(number))]) % 7 == 0]))
print(sum([number for number in numbers_2 if sum([int(i) for i in list(str(number))]) % 7 == 0]))
print(sum([number + 17 for number in numbers_1 if sum([int(i) for i in list(str(number + 17))]) % 7 == 0]))
