# Resolução do professor Guanabara do desafio087. Matriz 3x3 de (0,0) até (2,2).
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = maior_linha2 = soma_coluna3 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número natural para ({linha},{coluna}): '))
print('=-=' * 15)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
        print()
print('=-=' * 15)
print(f'A soma dos valores é {soma_par}.')
for linha in range(0, 3):
    soma_coluna3 += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {soma_coluna3}')
for c in range(0, 3):
    if c == 0:
        maior_linha2 = matriz[1][c]
    elif matriz[1][c] > maior_linha2:
        maior_linha2 = matriz[1][c]
print(f'O maior valor da segunda linha é {maior_linha2}')
