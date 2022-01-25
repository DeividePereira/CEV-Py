import datetime
pessoa = dict()

pessoa['nome'] = str(input('Digite o seu nome: '))

pessoa['nasc'] = int(input('Digite o seu ano de nascimento: '))
while pessoa['nasc'].__class__ != int:
    print('Erro! Tente novamente.')
    pessoa['nasc'] = int(input('Digite o seu ano de nascimento: '))

pessoa['ctps'] = int(input('Digite a sua CTPS (se não houver, digite 0): '))
while pessoa['ctps'].__class__ != int:
    print('Erro! Tente novamente.')
    pessoa['ctps'] = int(input('Digite a sua CTPS: '))

pessoa['anoc'] = int(input('Digite o ano de contratação: '))
while pessoa['anoc'].__class__ != int and datetime.date.today.year() > pessoa['anoc'] > (datetime.date.today.year - 130): #erro
                                    #2022 > 2000 > (2022 - 130) = 2022 > 2000 > 1892 -> correto
    print('Erro! Tente novamente.')
    pessoa['anoc'] = int(input('Digite o ano de contratação: '))

pessoa['idade'] = datetime.date.today().year - pessoa['nasc']

if pessoa['ctps'] != 0:
    pessoa['aposentar'] = 35 - pessoa['ctps']
else:
    pessoa['aposentar'] = 35

print(pessoa)
print(pessoa['idade']) #teste
print(f'O(A) {pessoa["nome"]} irá se aposentar em {pessoa["aposentar"]} anos.')
print(pessoa['ctps'])
#print(pessoa['ctps'])