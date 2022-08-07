nc = '\033[m'
rc = '\033[31m'
ic = '\033[40m'
n = int(input('Digite um número inteiro: '))
print(f'Digite:\n{ic}[1]{nc} - Para Binário\n{ic}[2]{nc} - Para Octal\n{ic}[3]{nc} - Para Hexadecimal\n')
d = int(input('Qual é a base de conversão desejada? '))
while d < 1 or d > 3:
    print(f'{rc}Opção inválida! Tente novamente.{nc}')
    d = int(input('Qual é a base de conversão desejada? '))
if d == 1:
    print(f'{d} em binário é: {bin(n)[2:]}')
elif d == 2:
    print(f'{d} em octal é: {oct(n)[2:]}')
elif d == 3:
    print(f'{d} em hexadecimal é: {hex(n)[2:]}')
