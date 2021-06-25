dados = list()
pessoas = list()
nome_maior_peso = list()
nome_menor_peso = list()
num = maior_peso = menor_peso = 1

while True:
    nome = str(input(f'Digite o nome da pessoa n°{num}: ')).strip().title()
    while nome.isnumeric() or len(nome) == 0:
        print('\033[31mResposta inválida! Tente novamente.\033[m')
        nome = str(input(f'Digite o nome da pessoa n°{num}: ')).strip().title()
    dados.append(nome)

    peso = float(input(f'Digite o peso, em kg, da pessoa n°{num}: '))
    while str(peso).isalpha():
        print('\033[31mResposta inválida! Tente novamente.\033[m')
        peso = float(input(f'Digite o peso, em kg, da pessoa n°{num}: '))

    if num == 1:    #Usando o primeiro peso como parâmetro, marcando o dono pelo num.
        maior_peso = peso
        nome_maior_peso.append(nome)
        menor_peso = peso
        nome_menor_peso.append(nome)
    else:
        if peso > maior_peso:
            maior_peso = peso
            nome_maior_peso.clear()
            nome_maior_peso.append(nome)

        elif peso == maior_peso:
            nome_maior_peso.append(nome)

        elif peso < menor_peso:
            menor_peso = peso
            nome_menor_peso.clear()
            nome_menor_peso.append(nome)

        elif peso == menor_peso:
            nome_menor_peso.append(nome)

    dados.append(peso)
    pessoas.append(dados[:])  #Passando a lista dados para a lista pessoas.
    dados.clear()

    user = str(input('Deseja continuar?\033[40m[S/N]\033[m ')).upper()
    while user != 'N' and user != 'S' or user.isspace() or user.isnumeric() or len(user) == 0:
        print('\033[31mResposta inválida! Tente novamente.\033[m')
        user = str(input('Deseja continuar?\033[40m[S/N]\033[m ')).upper()
    if user == 'N':
        break
    elif user == 'S':
        num += 1

print('=-=' * 15)
print(f'Foram cadastradas {num} pessoas.')
print(pessoas)
print(f'O maior peso é {maior_peso:.2f}kg, que pertence a: {nome_maior_peso}')
print(f'O menor peso é {menor_peso:.2f}kg, que pertence a: {nome_menor_peso}')
