"""3 comprimento de reta: formam um triângulo?"""
a = float(input('Um dos comprimentos é: '))
b = float(input('Um dos outros comprimentos é: '))
c = float(input('O outro comprimento é: '))
if a + b > c and a + c > b and b + c > a:
    print('Forma um triângulo.')
else:
    print('Não forma um triângulo.')
