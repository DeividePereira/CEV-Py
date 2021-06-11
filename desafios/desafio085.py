lista = ([], [])
for n in range(1, 7):
    num = int(input(f'Digite o {n}° número natural: '))
#    while str(num).isalpha():                           #Não funciona
#        print('Resposta inválida! Tente novamente.')
#        num = int(input(f'Digite o {n}° número natural: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print(lista)
print(f'Os números pares são: {sorted(lista[0])}')
print(f'Os números ímpares são: {sorted(lista[1])}')
