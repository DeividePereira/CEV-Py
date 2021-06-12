#matriz NxN, o usuário deve determinar N. Desafio proposto por mim mesmo.
list = ([], [], [], [], [], [], [], [], [])
x = y = n = a = b = e = ex = 0

print('Uma matriz quadrada é composta por linha e coluna de mesmo tamanho, ou seja, uma matriz AxA.')
exemplo = ([], [], [], [])
print('Exemplo de uma matriz 2x2: ')
for e in exemplo:
    for ex in e:
        print(f'[ {ex:^5} ]', end=' ')
        if ex != 0 and ex % 2 == 0:
            print('\n')

user = int(input('Determine o N da matriz quadrada: '))
if user < 1:
    print('Uma matriz deve ser maior que 1. Tente novamente.')
    while user < 1:
        print('Uma matriz deve ser maior que 1. Tente novamente.')
        user = int(input('Determine o N da matriz quadrada: '))

sudo = user * user  #Limite da matriz; Quantidade de posições.

for n in range(0, sudo):
    valor = int(input(f'Digite um valor inteiro do elemento {x+1}x{y+1}: '))

    if x == user:    #((0,0), (1,0),..., (user,0) (0,1), (1,1),..., (user,1),..., (user, user)
        x = 0
        y += 1
    elif x == user and y == user:  #Fim da matriz NxN
        break
    else:
        x += 1
    list[n].append(valor)     #len(list) == n -> é o número de lista
    n += 1                   #IndexError: tuple index out of range; quando n = 5.

for a in list:     #a é cada item da list.
    for b in a:    #b é cada item de cada lista, ou subitem da list.
        if b < 6:
            print(f'| {b}', end=' | ')
        else:  #b >= 6:
            print(f'| {b}', end=' | ')
        if b != 0 and b % user == 0:
            print('\n', end='')
