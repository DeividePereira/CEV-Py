# vários números, coloque-os numa lista
# A) quantos números foram digitados
# B) a lista de núm de forma decrescente
# C) se o valor 5 foi digitado ou está na lista.
# todos estão com erro
list = []
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

print(f'Foram dados {len(list)} números.')
# list_rev = list.sort()[::-1]  #TypeError: 'NoneType' object is not subscriptable
# print(f'A lista decrescente é:\n{list_rev}')  #erro: <built-in method reverse of list object at 0x7f46c0e194c0>
# print(f'A lista decrescente é:\n{list.reverse()}')  #erro: "None"
list.sort()
list_rev = list[::-1]
print(f'A lista decrescente é:\n{list_rev}')
print(f'O número 5 apareceu {list.count("5")} vezes.')
