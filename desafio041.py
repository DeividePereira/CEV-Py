import datetime
nasc = int(input('Digite o ano de nascimento do atleta: '))
atual = datetime.date.today().year
i = atual - nasc
print(f'O atleta tem {i} anos.')
if i <= 9:
    print('Sua categoria é Mirim.')
elif i <= 14:
    print('Sua categoria é Infantil.')
elif i <= 19:
    print('Sua categoria é Junior.')
elif i <= 25:
    print('Sua categoria é Sênior.')
else:
    print('Sua categoria é Master.')
if i == 10:
    print(i)