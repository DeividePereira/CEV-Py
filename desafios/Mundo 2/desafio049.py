i = int(input('Digite de qual número inteiro deseja a tabuada: '))
print('='*20)
for a in range(1, 101):  #Era pra ser 11, botei 101.
    print(f'{i} * {a:2} = {i * a:2}')
print('='*20)
