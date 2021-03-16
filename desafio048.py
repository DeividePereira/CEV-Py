soma = cont = 0
print('Os números ímpares e múltiplos de três que encontram-se entre 0 e 500;')
for e in range(1, 501, 2):
    if e % 3 == 0:
        soma += e
        cont += 1
print(f'Tem no total {cont} elementos;\nE a soma deles é {soma}.')
