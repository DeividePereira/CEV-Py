import datetime
pessoa = dict()

pessoa['nome'] = str(input('Digite o seu nome: '))
#while not pessoa['nome'].isalpha == True:
#    print('Erro! Tente novamente.')
#    pessoa['nome'] = str(input('Digite o seu nome: '))

pessoa['nasc'] = int(input('Digite o seu ano de nascimento: '))
while pessoa['nasc'] < datetime.date.today().year - 130 or pessoa['nasc'] > datetime.date.today().year + 1:
    print('Erro! Tente novamente.')
    pessoa['nasc'] = int(input('Digite o seu ano de nascimento: '))

pessoa['idade'] = datetime.date.today().year - int(pessoa['nasc'])

pessoa['ctps'] = int(input('Digite a sua CTPS (se não houver, digite 0): '))
while pessoa['ctps'] < 0:
    print('Erro! Tente novamente.')
    pessoa['ctps'] = int(input('Digite a sua CTPS (se não houver, digite 0): '))

if pessoa['ctps'] != 0:
    pessoa['anoc'] = int(input('Digite o ano de contratação: '))
    pessoa['sal'] = float(input('Digite o salário: '))
    pessoa['aposentar'] = pessoa['anoc'] + 35#É a idade que se aposenta ou quanto tempo falta?
#    while datetime.date.today().year() + 1 < pessoa['anoc'] < datetime.date.today().year - 130:
#                                      2023 <     2000       < 1892
#        print('Erro! Tente novamente.')
#        pessoa['anoc'] = int(input('Digite o ano de contratação: '))
else:
    pessoa['aposentar'] = 35

print('-=' * 25)
print(f'O nome da pessoa é: {pessoa["nome"]}')
print(f'A idade é: {pessoa["idade"]}')
print(f'A CTPS tem valor: {pessoa["ctps"]}')
if pessoa['ctps'] != 0:
    print(f'Ano de contratação: {pessoa["anoc"]}')
    print(f'Salário: R${pessoa["sal"]:.2f}')
    print(f'O(A) {pessoa["nome"]} irá se aposentar em {pessoa["aposentar"]}.')
