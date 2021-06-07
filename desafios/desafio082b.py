# Colocar todos em uma lista -> copiar para as duas outras listas -> separar em impares e pares
# versão com num = int() e a passagem pras duas listas diferente.
list = list()
list_even = []
list_odd = []
user = 0
while user != 'N':
    num = int(input('Digite um número: '))
    if list.count(num) == 0:  #Checando se o valor é único.
        list.append(num)

    user = str(input('Você gostaria de continuar?\033[40m[S/N]\033[m ')).strip().upper()
    while user != 'S' and user != 'N' or user.isspace() or user == '':
        print('\033[31mResposta inválida! Tente novamente!\033[m')
        user = str(input('Você gostaria de continuar?\033[40m[S/N]\033[m ')).strip().upper()
        if user == 'N':
            break
    if user == 'N':
        break

for a in list:  # par
    if a % 2 == 0:
        list_even.append(a)

for b in list:  # ímpar
    if b % 2 != 0:
        list_odd.append(b)

print(f'\nLista: {list}')
print(f'Lista com os números pares: {list_even}')
print(f'Lista com os números ímpares: {list_odd}')
