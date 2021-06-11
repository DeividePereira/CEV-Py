# Nome e peso de várias pessoas, tudo isso em uma lista///
# A) Quantas pessoas foram cadastradas///
# B) Uma listagem com as pessoas mais pesadas
# C) e uma com os mais leves.
# versão com str, mas dará erro quando for re
dados = []
pessoas = []
num = 1
while True:
    nome = str(input(f'Digite o nome da pessoa n°{num}: ')).strip().title()
    while nome.isnumeric() or len(nome) == 0:
        print('Resposta inválida! Tente novamente.')
        nome = str(input(f'Digite o nome da pessoa n°{num}: ')).strip().title()
    dados.append(nome)

    peso = str(input(f'Digite o peso da pessoa n°{num}: ')).strip()
    while peso.isalpha() or len(peso) == 0:
        print('Resposta inválida! Tente novamente.')
        peso = str(input(f'Digite o peso da pessoa n°{num}: ')).strip()
    dados.append(peso)
    pessoas.append(dados[:])  #Passando a lista dados para a lista pessoas.
    dados.clear()

    user = str(input('Deseja continuar?\033[40m[S/N]\033[m ')).upper()
    while user != 'N' and user != 'S' or user.isspace() or user.isnumeric():
        print('Resposta inválida! Tente novamente.')
        user = str(input('Deseja continuar?\033[40m[S/N]\033[m ')).upper()
    if user == 'N':
        break
    elif user == 'S':
        num += 1
print(f'Foram cadastradas {num} pessoas.')
print(pessoas)
print(pessoas.sort())   # == None
print(pessoas.sort()[0:2])  #TypeError: 'NoneType' object is not subscriptable
pessoas_pesadas = pessoas.sort()[0:2:-1]   #Checar
print(pessoas_pesadas)
print(f'As duas pessoas mais pesadas são: {int(pessoas_pesadas)}')

#pessoas_leves = pessoas.sort()
