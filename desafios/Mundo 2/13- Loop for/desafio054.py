"""maioridade = 21 anos"""
from datetime import date
maior = menor = nasc = 0
atual = date.today().year

for ano in range(1, 8):
    nasc = int(input('Digite o ano de uma pessoa nascimento: '))
    i = atual - nasc

    if i >= 21:
        maior += 1
    elif i < 21:
        menor += 1

print(f'\033[31m{maior}\033[m são maiores de idade;\n\033[33m{menor}\033[m são menores de idade.')
