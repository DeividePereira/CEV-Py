list = list()
user = 0
while user != 'N':
    num = str(input('Digite um número: '))
    while not num.isnumeric():
        num = str(input('Digite um número: '))
    if list.count(num) == 0:  #Checando se o valor é único.
        list.append(num)

    user = str(input('Você gostaria de continuar?\033[40m[S/N]\033[m ')).strip().upper()
    while user != 'S' and user != 'N' or user.isspace() or user == '':  #Checando se foi S ou N.
        print('\033[31mResposta inválida! Tente novamente!\033[m')
        user = str(input('Você gostaria de continuar?\033[40m[S/N]\033[m ')).strip().upper()
        if user == 'N':
            break
    if user == 'N':
        break

listpar = list[:]
listimpar = list[:]
posi = 0
#while posi < len(list):

print(f'Lista: {list}')
print(f'Lista com os números pares: {listpar}')
print(f'Lista com os números ímpares: {listimpar}')
