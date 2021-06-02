p1 = str(input('Digite o nome do produto 1: '))
c1 = float(input('Digite o preço do produto 1: '))
'''p2 = str(input('Digite o nome do produto 2: '))
c2 = float(input('Digite o preço do produto 2: '))
p3 = str(input('Digite o nome do produto 3: '))
c3 = float(input('Digite o preço do produto 3: '))
p4 = str(input('Digite o nome do produto 4: '))
c4 = float(input('Digite o preço do produto 4: '))'''
list = (p1, c1)  #, p2, c2, p3, c3, p4, c4)
defi = 'Listagem de Preços'
print('-' * 40, f'\n{defi:^40}')  #Dá um espaço se colocar junto
print('-' * 40)
print(f'{p1:.<28}', end=f'R${c1:.2f}')

