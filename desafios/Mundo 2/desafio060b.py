""" fatorial com repetição for   - 5! = 5*4*3*2*1 """

print('==-== \033[36mCálculo de Fatorial\033[m ==-==')
a = n1 = int(input('Digite um número inteiro qualquer: '))
acumulador = 1
for n1 in range(n1, 0, -1):
    acumulador *= n1
print(f'{a}! = {acumulador}')
