lista = ([], [])
for n in range(0, 6):
    num = int(input(f'Digite o {n + 1}° número natural: '))

    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print(lista)
print(f'Os números pares são: {sorted(lista[0])}')
print(f'Os números ímpares são: {sorted(lista[1])}')
