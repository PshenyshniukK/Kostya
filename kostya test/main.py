# Capitals = dict()
# Capitals['Ukraine'] = 'Kiev'
# Capitals['Spain'] = 'Madrid'
# Capitals['Italy'] = 'Rome'
#
#
# Countries = ['Ukraine', 'Spain','Italy']
# Countries = {'Ukraine': 'Kiev', 'Spain': 'Madrid', 'Italy': 'Rome'}
# print('Countries')
# for key in Countries:
#     print({Countries[key]})
# for value in Countries.values():
#     print(value)

# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
# for key in users:
#     print(f"Phone: {key}  User: {users[key]} ")
# Countries = {'Ukraine': 'Kiev', 'Spain': 'Madrid', 'Italy': 'Rome'}
#
# x = Countries.keys()
# y = Countries.values()
# print(x, y)




# countries = ['Ukraine', 'Spain', 'Italy']
# capitals = ['Kiev', 'Madrid', 'Rome']
#
# dictionary = dict(zip(countries, capitals))
# print(dictionary)


#
# list1 = ['Ukraine', 'Spain', 'Italy']
#
# dict1 = {'Ukraine': 'Kiev', 'Spain': 'Madrid', 'Italy': 'Rome'}
# for x in dict1:
#     for y in dict1:
#         print(x y)


Countries = ['Ukraine', 'Spain','Italy']
Countries1 = {'Ukraine': 'Kiev', 'Spain': 'Madrid', 'Italy': 'Rome'}
print('Ukraine: Kiev', 'Spain: Madrid', 'Italy: Rome', sep='\n')


data = ['Ukraine:Kiev', 'Spain:Madrid', 'Italy:Rome']
print(data[0].split(":")[0], data[0].split(":")[1], sep=': ')
print(data[1].split(":")[0], data[1].split(":")[1], sep=': ')
print(data[2].split(":")[0], data[1].split(":")[1], sep=': ')


Countries=['Ukraine', 'Spain', 'Italy']
Capitals=['Kiev', 'Madrid', 'Rome']
print('\n'.join(['{}\t{}'.format(*t) for t in zip(Countries,Capitals)]))