"""Feito pelo Prof. Guanabara"""

a = int(input('Qual o termo inicial? '))
r = int(input('Qual a razão? '))
t = a
cont = 1

while cont <= 10:
    print(f'{t}', end=" → ")
    t += r
    cont += 1
print('Fim')
