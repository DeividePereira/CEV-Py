"""Feito por Davi Luiz; Nant = Número anterior"""
Nant = 1
Fibonacci = 0

n = int(input('Digite um número:(Este vai ser o nº de elementos da sequência) '))

while n != 0:
    print('{}'.format(Fibonacci), end="\033[31m → \033[m")
    Fibonacci = Fibonacci + Nant
    Nant = Fibonacci - Nant
    n -= 1
print('FIM')
