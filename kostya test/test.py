lst = [1, 2, 3, 4, 5]
lst2 = []
for i in range(0, len(lst) - 1):
    n = (lst[i] + lst[i+1]) / 2
    lst.append(n)
print(lst)
print(sorted(lst))