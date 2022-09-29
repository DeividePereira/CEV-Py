from random import randint
lista = []
user = 0

while user != 'N':
    num = str(input('Digite um número: '))
    while not num.isnumeric():
        num = str(input('Digite um número: '))
    if lista.count(int(num)) == 0:  # Checando se o valor é único.
        lista.append(int(num))

    user = str(input('Você gostaria de continuar?\033[40m[S/N]\033[m ')).strip().upper()
    while user != 'S' and user != 'N' or user.isspace() or user == '':  # Checando se foi S ou N.
        print('\033[31mResposta inválida! Tente novamente!\033[m')
        user = str(input('Você gostaria de continuar?\033[40m[S/N]\033[m ')).strip().upper()
        if user == 'N':
            break
    if user == 'N':
        break

print(f'Foram dados {len(lista)} números\033[33m únicos\033[m.')

lista.sort()
list_rev = lista[::-1]
print(f'\033[36mA lista decrescente é:\n{list_rev}\033[m')
# poderia ser feito list.sort(reverse=True) // mas precisaria estar como int.


if lista.count(5) == 0:  # Poderia ser if 5 in list:
    print('O número 5 não apareceu na lista.')
else:
    print(f'O número 5 apareceu na lista.')

n_random = randint(min(lista), max(lista))  # Se há um número aleatório entre o mínimo e o máximo da lista.
if lista.count(n_random) == 0:
    print(f'O número aleatório, entre o maior e menor da lista, {n_random} não apareceu na lista.')
else:
    print(f'O número aleatório, entre o maior e menor da lista, {n_random} apareceu na lista.')
