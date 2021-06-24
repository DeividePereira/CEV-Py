#matriz NxN, o usuário deve determinar N. Desafio proposto por mim mesmo.
list = list()
list_elemento = []
ex_cont = contador = 0
y = x = 1
print('Uma matriz quadrada é composta por linha e coluna de mesmo tamanho, ou seja, uma matriz AxA.')
exemplo = ([1], [2], [3], [4])
print('Exemplo de uma matriz quadrada 2x2: ')
for e in exemplo:
    for ex in e:
        print(f'| {ex:^5} ', end='')
        if ex_cont != 0 and (ex_cont % 2) - 1 == 0:
            print('|\n', end='')
        ex_cont += 1
print('-' * 45)

user = int(input('Determine o N de uma matriz quadrada NxN: '))
while user < 1:
    print('\033[31mUma matriz deve ser maior que 1. Tente novamente!\033[m')
    user = int(input('Determine o N de uma matriz quadrada NxN: '))

sudo = user * user  #Quantidade de elementos.
print(f'Esta matriz terá {sudo} elementos.')
print('-' * 45)

for n in range(0, sudo):
    elemento = int(input(f'Digite um valor inteiro do elemento ({x},{y}): '))
    list_elemento.append(elemento)
    list.append(list_elemento[:])
    list_elemento.clear()

    if y == user:    #((0,0), (1,0),..., (user,0) (0,1), (1,1),..., (user,1),..., (user, user)
        y = 1
        x += 1
    elif x == user and y == user:  #Fim da matriz NxN
        break
    else:
        y += 1
    n += 1
print('-' * 45)
print(f'Sua matriz {user}x{user} é: ')
for a in list:     #a é cada item da list.
    for b in a:    #b é cada item de cada lista, ou subitem da list.
        print(f'| {b:^5} ', end='')

        if contador + 1 == user:
            print('|\n', end='')
            contador = 0
        else:
            contador += 1
