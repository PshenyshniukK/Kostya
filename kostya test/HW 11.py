
my_text = 'Hello all. Here is pretty cold and hot. Choose yourself'
par1 = my_text.split('. ')
list2 = []
for i in par1:
    list2.append(i)
print(list2)
list3 = []
for i in list2:
   print(len(i.split()), end=', ')


