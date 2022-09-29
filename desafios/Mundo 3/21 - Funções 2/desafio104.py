def leiaint(user):
    while not user.isnumeric():
        print('  \033[31mErro! Tente novamente.\033[m')
        user = str(input('Digite um número: '))
    print('-' * 30)
    print(f'Você digitou o número {user}.')


print('Verificador de entradas, apenas números são aceitos.')
leiaint(str(input('Digite um número natural: ').strip()))
