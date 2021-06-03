list = (str(input('Digite o nome do produto 1: ')), float(input('Digite o preço do produto 1: ', )),
        str(input('Digite o nome do produto 2: ')), float(input('Digite o preço do produto 2: ', )),
        str(input('Digite o nome do produto 3: ')), float(input('Digite o preço do produto 3: ', )),
        str(input('Digite o nome do produto 4: ')), float(input('Digite o preço do produto 4: ', )))
print('-' * 40)
print(f'{"Listagem de Preços":^40}')
print('-' * 40)

for posi in range(0, len(list)):
    if posi % 2 == 0:
        print(f'{list[posi]:.<30}')
    else:
        print(f'{list[posi]:7.2f}')

print('-' * 40)
