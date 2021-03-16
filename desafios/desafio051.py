# An = A1 + (n – 1) * r
a = int(input('Qual o termo inicial? '))
r = int(input('Qual a razão? '))
t = int(input('Quantos termos deseja? '))

print(f'Os {t} primeiros termos dessa PA são:')

for b in range(t, 0, -1):
    print(f'{a + (t - b) * r}', end=" → ")
    for d in range(0, t, 15):
        if b == d:
            print('\n')
print('Fim!')
