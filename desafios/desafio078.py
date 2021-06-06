from time import sleep

valores = list()
for val in range(0, 5):
    valores.append(int(input('Digite um valor numérico: ')))

print('\033[37m-\033[m' * 45)
print('Você digitou os valores: ', end='')
for z in valores:
    print(f'{z}', end=' ')

print('\n\033[37mProcessando...\033[m')
sleep(0.2)

maior = max(valores)
menor = min(valores)
print(f'O valor máximo é: {max(valores)}, nas posições: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i + 1}, ', end='')

print(f'\nO valor mínimo é: {min(valores)}, nas posições: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i + 1}, ', end='')
