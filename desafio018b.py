from math import sin, cos, tan, radians
a = float(input('Digite o ângulo, em graus: '))
print(f'Seu seno é: {(sin(radians(a))):.2f}')
print(f'Seu cosseno é: {(cos(radians(a))):.2f}')
print(f'Sua tangente é: {(tan(radians(a))):.2f}')
