# Melhoria do desafio086b; matriz NxN, o usuário deve determinar N. Desafio proposto por mim mesmo.
# a) a soma de todas os valores pares digitados; b) A soma dos valores da coluna 3; c) O maior valor da linha 2
# obs.: foi usado mais matemática do que programação(lista dentro de listas)
list = list()
list_elemento = []
ex_cont = contador = soma_pares = maior_l2 = soma_c3 = 0
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
    elemento = int(input(f'Digite um valor inteiro do elemento ({x},{y}): '))  #alterado para = 1
    # x: horizontal, altera a coluna; y: vertical, altera a linha. A ideia é preencher todas as COLUNAS e dps
    # alterar a LINHA e reiniciar a coluna.
    if elemento % 2 == 0:
        soma_pares += elemento
    list_elemento.append(elemento)
    list.append(list_elemento[:])
    list_elemento.clear()

    if user < 3:    #Menor que 3x3
        soma_c3 = 'Inválido, pois não existe terceira coluna.'
    elif y == 3:    #Parâmetro para terceira coluna.
        soma_c3 += elemento

    if y == 0 and x == 2:   #Parâmetro para segunda linha.
        maior_l2 = elemento
    elif x == 2 and elemento > maior_l2:
        maior_l2 = elemento

    if y == user:    #((1,1), (2,1),..., (user,1) (1,2), (2,2),..., (user,2),..., (user, user)
        y = 1
        x += 1
    elif y == user and x == user:  #Fim da matriz NxN
        break
    else:
        y += 1      #A contagem de x e y está incorreta.
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
print('-' * 45)
print(f'O somatório dos números pares é: {soma_pares}')
print(f'O somatório dos números da terceira coluna é: {soma_c3}')
print(f'O maior valor da segunda linha é: {maior_l2}')
