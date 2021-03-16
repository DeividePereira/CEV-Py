from datetime import date
nasc = int(input('Ano de nascimento: ').strip())
atual = date.today().year
i = atual - nasc
print('Se você for do sexo masculino', end="")
if i < 17:
    saldo = 18 - i
    print(f', faltam {saldo} anos para você se alistar.')
    print(f'Seu alistamento militar será em {atual + saldo}.')
elif i == 17:  # 2021 - 17 = 2002
    print(f' e completa 18 anos até 29 de dezembro de {atual}', end="")
    print(', você deve procurar a junta militar mais próxima para se alistar.')
    print('Se não se alistou, você está atrasado com suas obrigações civis.')
elif i == 18:  # 2021-18 = 2003
    print(f', e completou 18 anos em {atual}, você deve procurar a junta militar mais próxima para se alistar.')
else:
    saldo = i - 18
    print(f', você deveria ter se alistado a {saldo} anos.')
    print(f'Seu alistamento foi em {atual - saldo}.')