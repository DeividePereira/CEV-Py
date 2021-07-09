from time import sleep
boletim = list()        #Lista universo
aluno = list()          #Sublista de boletim
notas = list()          #Sublista da aluno
media_list = list()
num = 1
empresa = "Boletim da Escola Ant\'s Harpoon"
print('-' * 45)
print(f'{empresa:^45}')
print('-' * 45)
while True:
    nome = str(input(f'Digite o nome do aluno n°{num}: ')).title().strip()
    while nome.isnumeric() or len(nome) == 0:
        print('\033[31mResposta inválida! Tente novamente.\033[m')
        nome = str(input(f'Digite o nome do aluno n°{num}: ')).title().strip()

    nota1 = float(input(f'Digite a nota 1 do aluno n°{num}: '))
    while str(nota1).isalpha() or str(nota1).isspace() or nota1 > 10 or nota1 < 1:
        print('\033[31mResposta inválida! Tente novamente.\033[m')
        nota1 = float(input(f'Digite a nota 1 do aluno n°{num}: '))

    nota2 = float(input(f'Digite a nota 2 do aluno n°{num}: '))
    while str(nota2).isalpha() or str(nota2).isspace() or nota2 > 10 or nota2 < 1:
        print('\033[31mResposta inválida! Tente novamente.\033[m')
        nota2 = float(input(f'Digite a nota 2 do aluno n°{num}: '))

    media = (nota1 + nota2) / 2
    aluno.append(nome)      #nome == aluno[0]
    notas.append(nota1)     #nota1 == notas[0]
    notas.append(nota2)     #nota2 == notas[1]
    aluno.append(notas[:])
    boletim.append(aluno[:])
    media_list.append(media)
    boletim[num - 1].append(media_list[:])     #boletim[0][2][0] == media
    aluno.clear()
    notas.clear()
    media_list.clear()

    user = str(input('Deseja continuar?\033[40m[S/N]\033[m')).upper().strip()
    while user.isnumeric() or len(user) == 0 or user != 'N' and user != 'S':
        print('\033[31mResposta inválida! Tente novamente.\033[m')
        user = str(input('Deseja continuar?\033[40m[S/N]\033[m')).upper()
    if user == 'N':
        break
    elif user == 'S':
        num += 1

    # boletim = ((aluno, media), (aluno, media))
    # boletim = (((nome, (nota1, nota2)), media), (((nome, (nota1, nota2)), media)))
    # boletim[0]        = (nome, (nota1, nota2)) --> ['Aang', [3.0, 4.0]]
    # boletim[0][0]     = nome                   --> Aang
    # boletim[0][1]     = notas                  --> [3.0, 4.0]
    # boletim[0][1][0]  = nota1                  --> 3.0
    # boletim[0][1][1]  = nota2                  --> 4.0
    # boletim[0][2][0]  = media                  --> 3.5
    # print(boletim)    --> [['Aang', [3.0, 4.0], [3.5]], ['Anna', [9.0, 10.0], [9.5]]]
    # print(boletim[0]) --> ['Aang', [3.0, 4.0], [3.5]]
    # print(boletim[1]) --> ['Anna', [9.0, 10.0], [9.5]]

print('-' * 45)
print(f'{"N°":<4}| {"Nome":<30}| {"Média":<4}')
for b in range(0, num):
    print(f'{b + 1:<4}| {boletim[b][0]:<30}| {boletim[b][2][0]:<4.1f}')
print('-' * 45)
while True:
    sudo = str(input('Deseja ver as notas de algum aluno?\033[40m[S/N]\033[m ')).upper().strip()
    while sudo.isnumeric() or len(sudo) == 0 or sudo.isspace() or sudo.isdecimal() or sudo != 'N' and sudo != 'S':
        print('\033[31mResposta inválida! Tente novamente.\033[m')
        sudo = str(input('Deseja ver as notas de algum aluno?\033[40m[S/N]\033[m ')).upper().strip()

    if sudo == 'S':
        ver = int(input('Digite o número do aluno para ver suas notas: '))
        while ver > num or ver <= 0:
            print('\033[31mResposta inválida! Tente novamente.\033[m')
            ver = int(input('Digite o número do aluno para ver suas notas: '))
        print('-' * 45)
        print(f'N°{ver} | {boletim[ver - 1][0]} | Nota 1: {boletim[ver - 1][1][0]} | Nota 2: {boletim[ver - 1][1][1]}')
        print('-' * 45)
    elif sudo == 'N':
        print('Tenha um bom dia!')
        break
print('Encerrando...')
sleep(1)
