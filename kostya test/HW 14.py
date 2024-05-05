list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print([i for i in list1 if i % 3 == 0 and not i % 5 == 0])
print([i for i in list1 if i % 5 == 0 and not i % 3 == 0])
print([i for i in list1 if i % 3 == 0 and i % 5 == 0])