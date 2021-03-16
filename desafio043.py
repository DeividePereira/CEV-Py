"""imc = peso/(altura * altura)"""
p = float(input('Insira o peso da pessoa, em quilos: ').strip())
a = float(input('Insira a altura da pessoa, em metros: '))

imc = p / (a * a)
print(f'{imc:.1f}')

print('Está', end=' ')
if imc < 18.5:
    print('abaixo do peso!')
elif 18.5 <= imc < 25:
    print('no peso ideal!')
elif 25 <= imc < 30:
    print('com sobrepeso!')
elif 30 <= imc < 40:
    print('com obesidade!')
else:
    print('com obesidade mórbida!')
