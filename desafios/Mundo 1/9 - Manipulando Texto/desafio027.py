nc = str(input('Digite seu nome completo: ')).strip()
d = nc.split()
print(f'O seu primeiro nome é: {d[0]}')
print(f'O seu último nome é: {d[len(d)-1]}')
