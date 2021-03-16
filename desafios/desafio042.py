a = float(input('Um dos comprimentos é: '))
b = float(input('Um dos outros comprimentos é: '))
c = float(input('O outro comprimento é: '))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Forma um triângulo equilátero.')
    elif a == b != c or a == c != b or b == c != a:
        print('Forma um triângulo isósceles.')
    elif a != b != c != a:
        print('Forma um triângulo escaleno.')
else:
    print('Não forma um triângulo.')
