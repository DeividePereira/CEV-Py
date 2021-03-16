n = int(input('Digite um número inteiro: '))
print('Digite:\n1 - Para Binário\n2 - Para Octal\n3 - Para hexadecimal\n')
d = int(input('Qual é a base de conversão desejada? '))
if d == 1:
    print(f'{d} em binário é: {bin(n)[2:]}')
elif d == 2:
    print(f'{d} em octal é: {oct(n)[2:]}')
elif d == 3:
    print(f'{d} em hexadecimal é: {hex(n)[2:]}')
else:
    print('Opção inválida! Tente novamente.')
