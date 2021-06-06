from time import sleep

valores = list()
for val in range(0, 5):
    valores.append(int(input('Digite um valor numérico: ')))

print('\033[37m-\033[m' * 45)
print('Você digitou os valores: ', end='')
for z in valores:
    print(f'{z}', end=' ')

print('\n\033[37mProcessando...\033[m')
sleep(0.5)

print(f'O valor máximo é: {max(valores)}, na {valores.index(max(valores)) + 1}° posição.')
print(f'O valor mínimo é: {min(valores)}, na {valores.index(min(valores)) + 1}° posição.')
