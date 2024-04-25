Number_lines = int(input('Number lines is :'))
for i in range(Number_lines):
    if i == i:
        print(' ' * (Number_lines - i - 1) + '*' * (i+1))
