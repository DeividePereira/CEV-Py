#n = str(input('Digite um número natural entre 0 e 9999: ').strip())
#n.replace('', '0')
#print(f'Milhares: {n[0]}')
#print(f'Centenas: {n[1]}')
#print(f'Dezenas : {n[2]}')
#print(f'Unidades: {n[3]}')
#Não funciona para números menores que 1000

n = int(input('Digite um número natural entre 0 e 9999: ').strip())
n2 = str(int(10000 + n))
print(f'Milhares: {n2[1]}')
print(f'Centenas: {n2[2]}')
print(f'Dezenas : {n2[3]}')
print(f'Unidades: {n2[4]}')
# Tenta dar uma volta no problema anterior, mas é imperfeito.
