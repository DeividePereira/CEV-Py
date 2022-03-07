dici = dict()
lista_dicis = list()
soma_idade = 0
mulheres = list()
idade_acima = list()

num_pessoas = int(input('Quantas pessoas deseja cadastrar? '))
while num_pessoas <= 0:
    print('Erro! Tente novamente.')
    if num_pessoas > 10:
        print('O número máximo para cada vez é 10.')
    num_pessoas = int(input('Quantas pessoas deseja cadastrar? '))

for a in range(1, num_pessoas + 1):
    dici['nome'] = str(input(f'Digite o nome da {a}ª pessoa: ')).title()
    while len(dici['nome']) == 0:
        print('   Erro! Tente novamente.')
        dici['nome'] = str(input(f'Digite o nome da {a}ª pessoa: ')).title()
    
    dici['sexo'] = str(input('Digite \"M\" para masculino ou \"F\" para feminino;\nOu \"NB\" para não-binário: ')).upper()
    while dici['sexo'] != 'M' and dici['sexo'] != "F" and dici['sexo'] != "NB":
        print('   Erro! Tente novamente.')
        dici['sexo'] = str(input('Digite \"M\" para masculino \"F\" para feminino e \"NB\" para não binário: ')).upper()
    
    if dici['sexo'] == 'F':
        mulheres.append(dici['nome'])
    
    dici['idade'] = int(input(f'Digite a idade da {a}ª pessoa: '))
    while dici['idade'] < 0 or dici['idade'] > 130:
        print('   Erro! Tente novamente.')
        dici['idade'] = int(input(f'Digite a idade da {a}ª pessoa: '))
    
    soma_idade += dici['idade']
    lista_dicis.append(dici.copy())
    dici.clear()

media_idade = soma_idade / num_pessoas

for b in lista_dicis:
    if b['idade'] > media_idade:
        idade_acima.append(b['nome'])

print(f'Foram registradas {num_pessoas} pessoas.')
print(f'A média das idades é {media_idade:.2f}.')
print(f'As mulheres são: {mulheres}.', end="")
for c in {mulheres}:
    print(mulheres[c], end=', ')
print('\n')
print(f'As pessoas com idade acima da média de idade são: {idade_acima}')
