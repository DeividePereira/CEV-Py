n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))
if n1 > n2:
    print(f'O primeiro número, {n1}, é maior.')
elif n1 < n2:
    print(f'O segundo número, {n2}, é maior.')
else:
    print('Não há valor maior, pois os dois números são iguais.')
