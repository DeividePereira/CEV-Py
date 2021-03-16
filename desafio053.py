frase = str(input('Digite uma frase qualquer: ')).replace(' ', '').strip().upper()

print('O inverso de {} é {}'.format(frase, frase[::-1]))

if frase[::-1] == frase:
    print('Ou seja, a frase é um palíndromo.')

else:
    print('Ou seja, a frase não é um palíndromo.')
