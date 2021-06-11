# versão separação entre par e ímpar feita no início
from time import sleep
list = list()
list_par = []
list_impar = []
user = 0
while user != 'N':
    num = str(input('Digite um número: '))
    while not num.isnumeric():
        num = str(input('Digite um número: '))
    if list.count(int(num)) == 0:  #Checando se o valor é único.
        list.append(int(num))
        if int(num) % 2 == 0:  #Checando se é par.
            list_par.append(int(num))
        if int(num) % 2 != 0:  #Chechando se é ímpar.
            list_impar.append(int(num))

    user = str(input('Você gostaria de continuar?\033[40m[S/N]\033[m ')).strip().upper()
    while user != 'S' and user != 'N' or user.isspace() or user == '':  #Checando se foi S ou N.
        print('\033[31mResposta inválida! Tente novamente!\033[m')
        sleep(0.1)
        user = str(input('Você gostaria de continuar?\033[40m[S/N]\033[m ')).strip().upper()
        if user == 'N':
            break
    if user == 'N':
        break
print('-' * 50)
print(f'Lista: {list}')
print(f'Lista com os números pares: {list_par}')
print(f'Lista com os números ímpares: {list_impar}')
