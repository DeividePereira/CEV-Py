""" O desafio 069 não quebra. Entretanto, tive que remover o .strip.
Por isso, o input '    Masculino' não funcionaria, mas não finalizaria o programa. """

"""while True:
    print(f'\033[36mCadastro de Número 000\033[m')
    sexo = str(input('Sexo \033[40m[M/F]\033[m: ')).upper()  #MASCULINO

    if sexo[0] == ' ' or sexo[-1] == '':  #M
        sexo.strip()
        print(sexo.strip()[0])

    while sexo != 'M' and sexo != 'F' or sexo.isspace():
        print('\033[31mResposta inválida! Tente novamente!\033[m')
        sexo = str(input('Sexo \033[40m[M/F]\033[m: ')).upper()"""

"""while True:
    print(f'\033[36mCadastro de Número 000\033[m')
    sexo = str(input('Sexo \033[40m[M/F]\033[m: ')).upper()  #' Masculino ' -> ' MASCULINO '
    sexo2 = sexo.strip  # = 'MASCULINO'
    sexo3 = sexo2[0]  # 'M'

    while sexo2[0] != 'M' and sexo2[0] != 'F' or sexo.isspace() or sexo == '':
        print('\033[31mResposta inválida! Tente novamente!\033[m')
        sexo = str(input('Sexo \033[40m[M/F]\033[m: ')).upper()
Erro nos [0]"""

while sexo[0] != 'M' and sexo[0] != 'F' or sexo.isspace()[0]:
    print('\033[31mResposta inválida! Tente novamente!\033[m')
    sexo = str(input('Sexo \033[40m[M/F]\033[m: ')).upper()
