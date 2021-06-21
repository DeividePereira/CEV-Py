#matriz 3x3, começando do 0,0 -> 0,0
list = ([], [], [], [], [], [], [], [], [])
x = y = contador = 0
print('Uma matriz quadrada 3x3 é composta de 9 elementos.')
for n in range(0, 9):
    valor = int(input(f'Digite o valor inteiro do elemento ({x+1},{y+1}): '))  #Obs.: Apenas números

    if x == 2:    #((0,0), (1,0), (2,0), (0,1), (1,1), (2,1), (0,2), (1,2), (2,2))
        x = 0
        y += 1
    elif x == 2 and y == 2:  #Limite da matriz 3x3
        break
    else:
        x += 1
    list[n].append(valor)     #len(list) == n -> é o número de listas
    n += 1

for a in list:     #a é cada item da list.
    for b in a:    #b é cada item de cada lista, ou subitem da list.
        print(f'| {b:^5} ', end='')

        if contador != 0 and (contador % 3) - 2 == 0:  #(8 % 3)-2;
            print('|\n', end='')
        contador += 1
