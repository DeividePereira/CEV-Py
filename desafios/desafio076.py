p1 = str(input('Digite o nome do produto 1: ')).strip().title()
c11 = float(input('Digite o preço do produto 1: '))
p2 = str(input('Digite o nome do produto 2: ')).strip().title()
c21 = float(input('Digite o preço do produto 2: '))
'''p3 = str(input('Digite o nome do produto 3: ')).strip().title()
c3 = float(input('Digite o preço do produto 3: '))
p4 = str(input('Digite o nome do produto 4: ')).strip().title()
c4 = float(input('Digite o preço do produto 4: '))'''
c12 = f'R${c11:.2f}'  #Alterando para sempre ter duas casas decimais
c22 = f'R${c21:.2f}'  #E adicionando R$
list = (p1, c12, p2, c22)  #, p3, c3, p4, c4)
defi = 'Listagem de Preços'
print('-' * 40, f'\n{defi:^40}')  #Dá um espaço se colocar junto
print('-' * 40)
print(f'{p1:.<20}', end=f'{c12:.>20}')
print(f'\n{p2:.<20}', end=f'{c22:.>20}')
'''print(f'{p3:.<28}', end=f'{c3:.2f}')
print(f'{p4:.<28}', end=f'{c4:.2f}')'''
print('-' * 40)