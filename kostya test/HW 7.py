Number_lines = int(input('Number lines is :'))
for i in range(Number_lines+1):
    if i == i:
        print(' ' * (Number_lines - i) + '*' * (i+1))
