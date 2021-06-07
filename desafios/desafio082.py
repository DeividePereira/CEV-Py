# Colocar todos em uma lista -> copiar para as duas outras listas -> separar em impares e pares
# versão com num = str()
list = list()
list_even = []
list_odd = []
user = 0
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

for indice, valor in enumerate(list):
    if valor % 2 == 0:
        list_even.append(valor)
    if valor % 2 != 0:
        list_odd.append(valor)

print(f'Lista: {list}')
print(f'Lista com os números pares: {list_even}')
print(f'Lista com os números ímpares: {list_odd}')
