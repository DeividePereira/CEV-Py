a = int(input('Qual o termo inicial? '))
r = int(input('Qual a razão? '))
t = int(input('Quantos termos deseja? '))

print(f'Os {t} primeiros termos dessa PA são:')

while t > 0:
    print(f'{a + (t-1) * r}', end=" → ")
    t -= 1
    if t % 15 == 0:
        print('\n')
print('Fim')
