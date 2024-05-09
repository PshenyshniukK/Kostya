lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
min = 3
max = 6
for i in lst.copy():
    if i < min or i > max:
        lst.remove(i)
if len(lst) == 0:
    print('None')
else:
    print(sum(lst))

result = 1
for x in lst:
    result = result * x
if len(lst) == 0:
    print('None')
else:
    print(result)

