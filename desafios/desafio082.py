# Colocar todos em uma lista -> copiar para as duas outras listas -> separar em impares e pares
# versão com num = str()
list = list()
user = a = b = 0
while user != 'N':
    num = str(input('Digite um número: '))
    while not num.isnumeric():
        num = str(input('Digite um número: '))
    if list.count(int(num)) == 0:  #Checando se o valor é único.
        list.append(int(num))

    user = str(input('Você gostaria de continuar?\033[40m[S/N]\033[m ')).strip().upper()
    while user != 'S' and user != 'N' or user.isspace() or user == '':  #Checando se foi S ou N.
        print('\033[31mResposta inválida! Tente novamente!\033[m')
        user = str(input('Você gostaria de continuar?\033[40m[S/N]\033[m ')).strip().upper()
        if user == 'N':
            break
    if user == 'N':
        break

list_even = list[:]
print(f'Removendo da lista dos pares:', end='')
for a in list_even:  # par
    if a % 2 != 0:  # a % 2 != 0 -> resultados ímpares, remova-os
        print(f' {a}', end='')
        list_even.remove(a)

print(f'Removendo da lista dos ímpares:', end='')
list_odd = list[:]
for b in list_odd:  # ímpar
    if b % 2 == 0:  # b % 2 == 0 -> resultados pares, remova-os
        print(f' {b}', end='')
        list_odd.remove(b)

print(f'Lista: {list}')
print(f'Lista com os números pares: {list_even}')
print(f'Lista com os números ímpares: {list_odd}')
