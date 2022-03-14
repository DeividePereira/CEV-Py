n = soma = cont = 0
while True:
    n = int(input('Digite um número inteiro: \033[40m[999 para Parar]\033[m '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Foram digitados \033[31m{cont}\033[m números;')
print(f'A soma deles é \033[32m{soma}\033[m.')
