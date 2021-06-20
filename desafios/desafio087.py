# Melhoria do desafio086; matriz 3x3, começando do 0,0 -> 0,0; a) a soma de todas os valores pares digitados;
# b) A soma dos valores da terceira coluna; c) O maior valor da segunda linha
list = ([], [], [], [], [], [], [], [], [])
x = y = contador = soma_pares = maior_l2 = soma_c3 = 0
print('Uma matriz quadrada 3x3 é composta de 9 elementos.')
for n in range(0, 9):
    valor = int(input(f'Digite o valor inteiro do elemento ({x+1},{y+1}): '))  #Obs.: Apenas números
    if valor % 2 == 0:
        soma_pares += valor

    if x == 2:    #((0,0), (1,0), (2,0), (0,1), (1,1), (2,1), (0,2), (1,2), (2,2))
        x = 0
        y += 1
    elif x == 2 and y == 2:  #Limite da matriz 3x3
        break
    else:
        x += 1

    if n == 3:
        maior_l2 = valor
    else:
        if n == 4 or n == 5:
            if valor > maior_l2:
                maior_l2 = valor

    list[n].append(valor)     #len(list) == n -> é o número de listas
    n += 1
print('-' * 40, 'Sua matriz 3x3 é: ')
for a in list:     #a é cada item da list.
    for b in a:    #b é cada item de cada lista, ou subitem da list.
        print(f'| {b:^5} ', end='')

        if contador != 0 and (contador % 3) - 2 == 0:
            print('|\n', end='')
        contador += 1

c3 = list[2] + list[5] + list[8]
for s in c3:
    soma_c3 += s

print(f'O somatório dos números pares é: {soma_pares}')
print(f'O somatório dos números da terceira coluna é: {soma_c3}')
print(f'O maior valor da segunda linha é: {maior_l2}')
