

Countries1 = ['Ukraine', 'Spain','Italy']
Countries2 = {'Ukraine': 'Kiev', 'Spain': 'Madrid', 'Italy': 'Rome'}
print('Ukraine: Kiev', 'Spain: Madrid', 'Italy: Rome', sep='\n')


data = ['Ukraine:Kiev', 'Spain:Madrid', 'Italy:Rome']
print(data[0].split(":")[0], data[0].split(":")[1], sep=': ')
print(data[1].split(":")[0], data[1].split(":")[1], sep=': ')
print(data[2].split(":")[0], data[1].split(":")[1], sep=': ')


Countries3=['Ukraine', 'Spain', 'Italy']
Capitals=['Kiev', 'Madrid', 'Rome']
n = ':'
print('\n'.join(['{}:\t{}'.format(*t) for t in zip(Countries3, Capitals)]))

# Предыдущий код я оставил т.к. жалко удалять, ведь решения задачи были верными)))

Countries6 = ['Ukraine', 'Spain','Italy']
Countries7 = {'Ukraine': 'Kiev', 'Spain': 'Madrid', 'Italy': 'Rome'}
print(Countries6[0], Countries7['Ukraine'], sep=': ')
print(Countries6[1], Countries7['Spain'], sep=': ')
print(Countries6[2], Countries7['Italy'], sep=': ')


