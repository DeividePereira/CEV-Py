"""Usando o que aprendi na aula 15"""
print('==-== \033[36mSomatório de números inteiros\033[m ==-==')
cont = soma = n = maior = menor = 0
e = 'S'
while True:
    n = int(input('\033[40mDigite um número inteiro:\033[m '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    e = str(input('Deseja continuar?\033[40m[S/N]\033[m ')).strip().upper()[0]
    if e == 'N':
        break
    elif e != 'S' and e != 's' and e != 'N' and e != 'n':
        print('Valor inválido! Tente novamente.')
        e = str(input('Deseja continuar?\033[40m[S/N]\033[m ')).strip().upper()[0]

print(f'Foram \033[31m{cont}\033[m números;')
print(f'A soma é \033[32m{soma}\033[m;')
print(f'A média é \033[33m{soma / cont:.2f}\033[m;')
print(f'O maior é \033[34m{maior}\033[m, e o menor é \033[36m{menor}\033[m.')
