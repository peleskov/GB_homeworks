odd_to_number = (num for num in range(1, 16, 2))

for i in range(1, 18, 2):
    print(next(odd_to_number))
