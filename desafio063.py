"""Sequência de Fibonacci: 0-1-1-3-5-8-13-..."""
""" Feito pelo Prof. Guanabara """
print('-===- \033[36mSequência de Fibonacci\033[m -===-')
n = int(input('Quantos termos quer mostrar? '))
t1 = 0
t2 = 1

print(f'{t1}', end='')
print(f'\033[31m → \033[m', end="")
print(f'{t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'\033[31m → \033[m{t3}', end="")
    t1 = t2
    t2 = t3
    cont += 1

print(' → Fim!')
