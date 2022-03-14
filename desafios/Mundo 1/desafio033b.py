""" 3 números: qual o maior e qual o menor? """
# Feito por Mufasa e muito parecido com o do Prof. Guanabara

a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
c = int(input('Digite mais um número inteiro: '))
# Maior
if a > b and a > c:
    biggest = a
elif b > a and b > c:
    biggest = b
else:
    biggest = c
# Menor
if a < b and a < c:
    smallest = a
elif b < a and b < c:
    smallest = b
else:
    smallest = c
