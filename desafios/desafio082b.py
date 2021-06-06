# vários números, coloque-os numa lista///
# crie duas listas extras, uma com os valores impares e uma com os valores pares.
# mostre as três listas.///
from time import sleep
list = list()
list_par = list[:]
list_impar = list[:]
user = 0
while user != 'N':
    num = str(input('Digite um número: '))
    while not num.isnumeric():
        num = str(input('Digite um número: '))
    if list.count(num) == 0:  #Checando se o valor é único.
        list.append(num)
        if num % 2 == 0:  # não funciona
            list_par.append(num)
        if num % 2 != 0:
            list_impar.append(num)

    user = str(input('Você gostaria de continuar?\033[40m[S/N]\033[m ')).strip().upper()
    while user != 'S' and user != 'N' or user.isspace() or user == '':  #Checando se foi S ou N.
        print('\033[31mResposta inválida! Tente novamente!\033[m')
        sleep(0.1)
        user = str(input('Você gostaria de continuar?\033[40m[S/N]\033[m ')).strip().upper()
        if user == 'N':
            break
    if user == 'N':
        break

print(f'Lista: {list}')
print(f'Lista com os números pares: {list_par}')
print(f'Lista com os números ímpares: {list_impar}')
