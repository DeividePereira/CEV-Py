n = int(input('Digite um número natural entre 0 e 9999: ').strip())
m = n // 1000 % 10
c = n // 100 % 10
d = n // 10 % 10
u = n // 1 % 10
print(f'Milhares: {m}')
print(f'Centenas: {c}')
print(f'Dezenas : {d}')
print(f'Unidades: {u}')