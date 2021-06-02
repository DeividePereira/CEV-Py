cont9 = pares = 0
print('Digite apenas números inteiros cardinais entre 1 e 10')
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
d = int(input('Digite um número: '))

list = (a, b, c, d)
if list.count(9) == 0:
    print('O número 9 apareceu nenhuma vez.')
elif list.count(9) == 1:
    print(f'O número 9 apareceu 1 vez.')
else:
    print(f'O número 9 apareceu {list.count(9)} vez(es).')

if list.count(3) == 0:
    print('O número 3 apareceu nenhuma vez.')
else:
    print(f'O primeiro número 3 apareceu na {list.index(3) + 1}ª posição.')

for list in range(0, (len(list))):
    if list % 2 == 0:
        pares += 1
print(f'No total, houveram {pares} números pares.')
