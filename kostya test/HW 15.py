lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
min = 3
max = 6
for i in lst.copy():
    if i <= min or i >= max: # В ТЗ написано что обе границы инклюзивны, тоесть включены, если они включены, то и 3 и 6 должны убираться, соответсвенно я поставил в цикле <= и >= . Хотя в переписке и в ТЗ у вас сумма получилась 20, что свидетельствует что эти числа не включены в диапозон, В общем могу сделать итак и так
        lst.remove(i)
print(sum(lst))

result = 1
for x in lst:
    result = result * x
print(result)
