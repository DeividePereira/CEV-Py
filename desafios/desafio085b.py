lista = ([], [])
n = 1
while True:
    num = int(input(f'Digite o {n}° número natural: '))
#    while str(num).isalpha():                           #Não funciona
#        print('Resposta inválida! Tente novamente.')
#        num = int(input(f'Digite o {n}° número natural: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

    user = str(input('Deseja continuar?\033[40m[S/N]\033[m ')).upper()
    while user != 'N' and user != 'S' or user.isspace() or user.isnumeric():
        print('Resposta inválida! Tente novamente.')
        user = str(input('Deseja continuar?\033[40m[S/N]\033[m ')).upper()
    if user == 'N':
        break
    elif user == 'S':
        n += 1

print(f'Ao todo, foram {n} números.')
print(f'Os números pares são: {sorted(lista[0])}')
print(f'Os números ímpares são: {sorted(lista[1])}')
