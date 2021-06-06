user = str(input('Digite uma expressão matemática:\n'))
if (user.count('(') + user.count(')')) % 2 == 0:
    print('Essa expressão é\033[32m válida\033[m!')
else:
    print('Essa expressão é\033[31m inválida\033[m. Cheque os parênteses!')
# erro quando os parênteses estão invertidos.
# Exemplo: )x + 5( = 2
