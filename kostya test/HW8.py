minimum_width = int(input('minimum_width :'))
maximum_width = int(input('maximum_width :'))
test = int((maximum_width - minimum_width) / 2)
import math
for i in range(maximum_width - minimum_width + 1):
    if i == 0 or i == (maximum_width - minimum_width):
        print(' ' * test + '*' * minimum_width + ' ' * test)
    else:
        print(' ' * abs(test - i) + '*' + ' ' * range())
