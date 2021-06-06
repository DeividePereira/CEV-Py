user = str(input('Digite uma expressão matemática:\n'))
if (user.count('(') + user.count(')')) % 2 == 0:
    print('Essa expressão é \033[32mválida\033[m!')
else:
    print('Essa expressão é \033[31minválida\033[m. Cheque os parênteses!')
