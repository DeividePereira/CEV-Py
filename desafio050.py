s = 0
c = 0
for g in range(1, 7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 != 0:
        n = 0
    else:
        s += n
        c += 1
print(f'Dos 6 números, {c} são ímpares e a soma desses é {s}')
