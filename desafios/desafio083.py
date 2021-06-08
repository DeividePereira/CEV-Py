# Solução do Prof. Guanabara, mas está imperfeita
# Exemplo de erro:
user = str(input('Digite uma expressão matemática:\n'))
list = []
for simb in user:
    if simb == '(':
        list.append('(')
    elif simb == ')':
        if len(list) > 0:
            list.pop()
        else:
            list.append(')')
            break
if len(list) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
