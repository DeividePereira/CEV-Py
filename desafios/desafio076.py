p1 = str(input('Digite o nome do produto 1: ')).strip().title()
c1 = float(input('Digite o preço do produto 1: '))
p2 = str(input('Digite o nome do produto 2: ')).strip().title()
c2 = float(input('Digite o preço do produto 2: '))
list = (p1, c2, p2, c2)

print('-' * 40)
print(f'{"Listagem de Preços":^40}')
print('-' * 40)

for posi in range(0, len(list)):
    if posi % 2 == 0:
        print(f'{list[posi]:.<30}')
    else:
        print(f'{list[posi]:7.2f}')

print('-' * 40)
