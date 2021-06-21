# Melhoria do desafio086b; matriz NxN, o usuário deve determinar N. Desafio proposto por mim mesmo.
# a) a soma de todas os valores pares digitados; b) A soma dos valores da coluna 3; c) O maior valor da linha 2
list = list()
list_elemento = []
x = y = ex_cont = contador = soma_pares = maior_l2 = soma_c3 = 0
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
    elemento = int(input(f'Digite um valor inteiro do elemento ({x+1},{y+1}): '))
    list_elemento.append(elemento)
    if x == user:    #((0,0), (1,0),..., (user,0) (0,1), (1,1),..., (user,1),..., (user, user)
        x = 0
        y += 1
    elif x == user and y == user:  #Fim da matriz NxN
        break
    else:
        x += 1
    list.append(list_elemento[:])
    list_elemento.clear()
    n += 1

print('-' * 45)
for a in list:     #a é cada item da list.
    for b in a:    #b é cada item de cada lista, ou subitem da list.
        print(f'| {b:^5} ', end='')

        if contador + 1 == user:
            print('|\n', end='')
            contador = 0
        else:
            contador += 1
# deve haver \n quando a coluna for N, ou seja, quando o contador == user.

print(f'{list}')
