# Um programa que lê um nome e duas notas em uma lista composta. Mostre um boletim contendo a média de cada aluno.
# Permita que o usuário possa mostrar as notas individuais de cada aluno.
# repetição while: nome, nota 1, nota 2, quer continuar[S/N]?. -> Boletim -> Mostrar notas de qual aluno? (Número)
boletim = list()        #Lista universo
aluno = list()          #Sublista de boletim
notas = list()          #Sublista da aluno
num = 1
while True:
    nome = str(input(f'Digite o nome do aluno n°{num}')).title().strip()
    while nome.isnumeric() or len(nome) == 0:
        print('\033[31mResposta inválida! Tente novamente.\033[m')
        nome = str(input(f'Digite o nome do aluno n°{num}')).title().strip()

    nota1 = float(input(f'Digite a nota 1 do aluno n°{num}'))
    while str(nota1).isalpha() or str(nota1).isspace():
        print('\033[31mResposta inválida! Tente novamente.\033[m')
        nota1 = float(input(f'Digite a nota 1 do aluno n°{num}'))

    nota2 = float(input(f'Digite a nota 2 do aluno n°{num}'))
    while str(nota2).isalpha() or str(nota2).isspace():
        print('\033[31mResposta inválida! Tente novamente.\033[m')
        nota2 = float(input(f'Digite a nota 2 do aluno n°{num}'))

    user = str(input('Deseja continuar?\033[40m[S/N]\033[m')).upper().strip()
    while user.isnumeric() or len(user) == 0:
        print('\033[31mResposta inválida! Tente novamente.\033[m')
        user = str(input('Deseja continuar?\033[40m[S/N]\033[m')).upper()

    media = (nota1 + nota2) / 2

    aluno.append(nome)      #nome == aluno[0]
    notas.append(nota1)     #nota1 == notas[0]
    notas.append(nota2)     #nota2 == notas[1]
    aluno.append(notas[:])
    boletim.append(aluno)
    # boletim: ((nome, media), (nome, media))
    # aluno: (nome, (nota1, nota2))
    # notas: (nota1, nota2)
