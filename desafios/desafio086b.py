#matriz NxN, o usuário deve determinar N. Desafio proposto por mim mesmo.
list = ([], [], [], [], [], [], [], [], [])
x = y = ex_cont = contador = 0
print('Uma matriz quadrada é composta por linha e coluna de mesmo tamanho, ou seja, uma matriz AxA.')
exemplo = ([1], [2], [3], [4])
print('Exemplo de uma matriz 2x2: ')
for e in exemplo:
    for ex in e:
        print(f'| {ex:^5} ', end='')
        if ex_cont != 0 and (ex_cont % 2) - 1 == 0:
            print('|\n', end='')
        ex_cont += 1
print('-' * 40)
user = int(input('Determine o N da matriz quadrada: '))
if user < 1:
    print('Uma matriz deve ser maior que 1. Tente novamente.')
    while user < 1:
        print('Uma matriz deve ser maior que 1. Tente novamente.')
        user = int(input('Determine o N da matriz quadrada: '))

sudo = user * user  #Limite da matriz; Quantidade de posições.

for n in range(0, sudo):
    valor = int(input(f'Digite um valor inteiro do elemento ({x+1},{y+1}): '))

    if x == user:    #((0,0), (1,0),..., (user,0) (0,1), (1,1),..., (user,1),..., (user, user)
        x = 0
        y += 1
    elif x == user and y == user:  #Fim da matriz NxN
        break
    else:
        x += 1
    list[n].append(valor)     #len(list) == n -> é o número de lista
    n += 1
    #IndexError: tuple index out of range; quando n > 3.
    # quando user > 3, o número de sublistas dentro de list passa de 9 e dá tuple index out of range.
    # deve ser feito list.append(sublista) para funcionar

for a in list:     #a é cada item da list.
    for b in a:    #b é cada item de cada lista, ou subitem da list.
        if contador < 6:
            print(f'| {b:^5} ', end='')
        else:  #contador >= 6:
            print(f'| {b:^5} ', end='')
        if user == 3:
            if contador != 0 and (contador % 3) - 2 == 0:  #Como consertar o '-2'? Só funciona para 3x3
                print('|\n', end='')
        contador += 1
