import math
minimum_width = int(input('minimum_width :'))
maximum_width = int(input('maximum_width :'))
test = int((maximum_width - minimum_width) / 2)
test2 = (minimum_width -2)
# parametr1 = list(range(minimum_width, maximum_width, 2))
# parametr2 = list(range(maximum_width - 4, minimum_width -1, -2))
print(parametr1)
print(parametr2)
for i in range(maximum_width - minimum_width + 1):
    if i == 0 or i == (maximum_width - minimum_width):
        print(' ' * test + '*' * minimum_width + ' ' * test)
    else:
        print(' ' * abs(test - i) + '*' + ' ' * (int(test2) + (i * 2)) + '*')
