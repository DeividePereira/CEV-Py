dados = list()
pessoas = list()
nome_maior_peso = list()
nome_menor_peso = list()
num = maior_peso = menor_peso = 1

while True:
    dados.append(str(input(f'Digite o nome da pessoa n°{len(pessoas) + 1}: ')).strip().title())
    while dados[0].isnumeric() or len(dados[0]) == 0:
        print('\033[31mResposta inválida! Tente novamente.\033[m')
        dados.append(str(input(f'Digite o nome da pessoa n°{len(pessoas) + 1}: ')).strip().title())

    dados.append(float(input(f'Digite o peso, em kg, da pessoa n°{len(pessoas) + 1}: ')))
    while str(dados[1]).isalpha():
        print('\033[31mResposta inválida! Tente novamente.\033[m')
        dados.append(float(input(f'Digite o peso, em kg, da pessoa n°{len(pessoas) + 1}: ')))   #Possível erro??

    if len(pessoas) == 0:    #Usando o primeiro peso como parâmetro, marcando o dono pelo num.
        maior_peso = dados[1]
        nome_maior_peso.append(dados[0])
        menor_peso = dados[1]
        nome_menor_peso.append(dados[0])
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
            nome_maior_peso.clear()
            nome_maior_peso.append(dados[0])

        elif dados[1] == maior_peso:
            nome_maior_peso.append(dados[0])

        elif dados[1] < menor_peso:
            menor_peso = dados[1]
            nome_menor_peso.clear()
            nome_menor_peso.append(dados[0])

        elif dados[1] == menor_peso:
            nome_menor_peso.append(dados[0])

    pessoas.append(dados[:])  #Passando a lista dados para a lista pessoas.
    dados.clear()

    user = str(input('Deseja continuar?\033[40m[S/N]\033[m ')).upper()
    while user != 'N' and user != 'S' or user.isspace() or user.isnumeric() or len(user) == 0:
        print('\033[31mResposta inválida! Tente novamente.\033[m')
        user = str(input('Deseja continuar?\033[40m[S/N]\033[m ')).upper()
    if user == 'N':
        break

print('=-=' * 15)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso é {maior_peso:.2f}kg, que pertence a: {nome_maior_peso}')
print(f'O menor peso é {menor_peso:.2f}kg, que pertence a: {nome_menor_peso}')
