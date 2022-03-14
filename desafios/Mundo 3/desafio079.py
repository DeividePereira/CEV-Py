from time import sleep
list = list()
user = 0
while user != 'N':
    valor = str(input('Digite um valor: '))
    while not valor.isnumeric():
        valor = str(input('Digite um valor: '))
    if list.count(valor) == 0:  #Checando se o valor é único.
        list.append(valor)
#    if valor not in list:
#        list.append(valor)
    user = str(input('Você gostaria de continuar?\033[40m[S/N]\033[m ')).strip().upper()
    while user != 'S' and user != 'N' or user.isspace() or user == '':  #Checando se foi S ou N.
        print('\033[31mResposta inválida! Tente novamente!\033[m')
        sleep(0.1)
        user = str(input('Você gostaria de continuar?\033[40m[S/N]\033[m ')).strip().upper()
        if user == 'N':
            break
    if user == 'N':
        break

print('-' * 50, '\nOs valores únicos, em ordem crescente, foram:')
list.sort()
for v in list:
    print(f'{v}', end=' ')
