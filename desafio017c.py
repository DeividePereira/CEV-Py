import math
print('Lembre-se de usar a mesma unidade de medida para os dois comprimentos.')
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print(f'A hipotenusa desse triângulo retângulo é: {math.hypot(co, ca):.2f}')
