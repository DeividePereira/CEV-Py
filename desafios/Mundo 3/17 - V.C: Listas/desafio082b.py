# Colocar todos em uma lista -> copiar para as duas outras listas -> separar em impares e pares
# versão com num = int() e a passagem pras duas listas diferente.
lista = list()
lista_even = []
lista_odd = []
user = 0
while user != 'N':
    num = int(input('Digite um número: '))
    if lista.count(num) == 0:  # Checando se o valor é único.
        lista.append(num)

    user = str(input('Você gostaria de continuar?\033[40m[S/N]\033[m ')).strip().upper()
    while user != 'S' and user != 'N' or user.isspace() or user == '':
        print('\033[31mResposta inválida! Tente novamente!\033[m')
        user = str(input('Você gostaria de continuar?\033[40m[S/N]\033[m ')).strip().upper()
        if user == 'N':
            break
    if user == 'N':
        break

for a in lista:
    if a % 2 == 0:
        lista_even.append(a)  # par
    else:
        lista_odd.append(a)  # ímpar

print(f'\nLista: {lista}')
print(f'Lista com os números pares: {lista_even}')
print(f'Lista com os números ímpares: {lista_odd}')
