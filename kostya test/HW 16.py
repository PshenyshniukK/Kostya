# lst = [10, 2, 3, 4, 5]
# lst2 = []
# for i in lst:
#     q = lst.index(i)
#     # e = lst.index(i+i)
#     print(q)
#     print(e)
#     w = (lst[q] + lst[e]) / 2
#     lst2.append(w)
# print(lst2)
# lst3 = []
# for i in lst:
#     lst3.append(i)
#     # print(lst3)
# for x in lst2:
#     y = lst2.index(x)
#     lst3.insert(y+y+1, x)
# print(lst3)


#
lst = [10, 5, 0, 2, 1]
lst2 = []
i = 0
while lst.index(lst[i]) != ValueError:
    lst2.append(lst[i])
    if i == len(lst)-1:
        break
    lst2.append((lst[i] + lst[i+1]) / 2)
    i += 1
print(lst2)




# for i in lst:
#     lst2.append(i)
#     if lst.index(i) <= len(lst) - 1:
#         lst2.append((i + i+1) / 2)
#         i += 1
# print(lst2)


# for i in lst:
#     n = (lst[i] + lst[i+1]) / 2
#     lst2.append(n)
# print(lst2)

# lst = [10, 11, 3, 4, 5]
# lst2 = []
# for i in lst:
#     n = lst[i] + lst[i+1]
#     print(n)

# arr = ['one', 'two', 'three', 'four']
# for i in range(0, len(arr), 2):
#     if i < len(arr) - 1:
#         print(arr[i], arr[i + 1])
#     else:
#         print(arr[i])
