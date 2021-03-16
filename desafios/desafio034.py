""" Acréscimo de salário.
Acima de 1250,00 +10%
Abaixo e igual a 1250: +15%"""
s = float(input('Digite o salário em reais: '))
if s > 1250:
    print(f'O acréscimo salarial é de R${s * (10/100):.2f}')
else:
    print(f'O acréscimo salarial é de R${s * (15/100):.2f}')
