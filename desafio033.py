""" 3 números: qual o maior e qual o menor? """

a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
c = int(input('Digite mais um número inteiro: '))

if a > b:  # se o A for maior que b
    d = a  # D = A (porque A é maior que B)
else:      # se não
    d = b  # D = B (porque B é maior que A)

if d > c:  # se o D (maior entre A e B) for maior que C
           # não precisa-se fazer algo, D já é o maior entre A,B e C
    print(f'O maior deles é {d}')
else:
    d = c  # D agora tem o valor de C, que é o maior entre A, B e C
    print(f'O maior deles é {c}')


if a < b:  # se o A for menor que b
    e = a  # D = A (porque A é maior que B)
else:      # se não
    e = b  # D = B (porque B é maior que A)

if e < c:  # se o D (maior entre A e B) for menor que C
           # não precisa-se fazer algo, D já é o menor entre A,B e C
    print(f'O menor deles é {e}')
else:
    e = c  # D agora tem o valor de C, que é o menor entre A, B e C
    print(f'O menor deles é {c}')
