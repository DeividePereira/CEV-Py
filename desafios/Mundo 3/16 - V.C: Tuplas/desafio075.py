cont9 = pares = 0
print('\033[33mPor favor, digite apenas números inteiros cardinais entre 1 e 10.\033[m')
list = (int(input('Digite um número: ')), int(input('Digite um número: ')),
        int(input('Digite um número: ')), int(input('Digite um número: ')))

if list.count(9) == 0:
    print('O número 9 não apareceu.')
elif list.count(9) == 1:
    print(f'O número 9 apareceu 1 vez.')
else:
    print(f'O número 9 apareceu {list.count(9)} vezes.')

if list.count(3) == 0:
    print('O número 3 não apareceu.')
else:
    print(f'O primeiro número 3 apareceu na {list.index(3) + 1}ª posição.')

for num in list:
    if num % 2 == 0:
        pares += 1
if pares == 0:
    print(f'No total, houve nenhum número par.')
elif pares == 1:
    print(f'No total, houve um número par.')
    print(f'O número par foi: ', end='')
    for num in list:
        if num % 2 == 0:
            print(num, end='')
else:
    print(f'No total, houveram {pares} números pares.')
    print(f'Os números pares foram: ')
    for num in list:
        if num % 2 == 0:
            print(num, end=' ')
