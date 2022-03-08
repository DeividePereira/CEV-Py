dici = dict()
l_dicis = list()
soma_idade = d = f = 0
l_mulheres = list()
d_idade_acima = dict()
l_d_idade_acima = dict()
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
    
    dici['sexo'] = str(input('Digite \"M\" para masculino ou \"F\" para feminino;\nOu \"NB\" para não-binário: ')).strip().upper()[0]
    while dici['sexo'] != 'M' and dici['sexo'] != "F" and dici['sexo'] != "NB":
        print('   Erro! Tente novamente.')
        dici['sexo'] = str(input('Digite \"M\" para masculino ou \"F\" para feminino;\nOu \"NB\" para não-binário: ')).strip().upper()[0]
    
    if dici['sexo'] == 'F':
        l_mulheres.append(dici['nome'])
    
    dici['idade'] = int(input(f'Digite a idade da {a}ª pessoa: '))
    while dici['idade'] < 0 or dici['idade'] > 130:
        print('   Erro! Tente novamente.')
        dici['idade'] = int(input(f'Digite a idade da {a}ª pessoa: '))
    
    soma_idade += dici['idade']
    l_dicis.append(dici.copy())
    dici.clear()

media_idade = soma_idade / num_pessoas
for b in l_dicis:
    if b['idade'] > media_idade:
        d_idade_acima['nome'] = b['nome']
        d_idade_acima['sexo'] = b['sexo']
        d_idade_acima['idade'] = b['idade']
        l_d_idade_acima.append(d_idade_acima.copy())
        d_idade_acima.clear()
print('-=' *30)
print(f'Foram registradas {num_pessoas} pessoas.')
print(f'A média das idades é {media_idade:.2f}.')
print(f'As mulheres são: ', end='')
for c in l_mulheres:
    print(f'{l_mulheres[d]}, ', end='')
    d += 1
print(f'\nAs pessoas com idade acima da média de idade são: ', end='')
for e in l_d_idade_acima:
    print(f'    Nome = {e["nome"]}; Sexo = {e["sexo"]}; Idade = {e["idade"]};')
print('\nEncerrando...')