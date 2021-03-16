maior = 0
menor = 0
for kg in range(1, 6, 1):
    peso = float(input(f'Peso, em kg, da {kg}ª pessoa: '))
    if kg == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior} kg;\nO menor peso é {menor} kg.')
