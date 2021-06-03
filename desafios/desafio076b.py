p1 = str('Um nome bem grande só pra testar mesmo')
'''c1 = 1234.567
print(f'R${c1:.2f}') #Alterando para sempre ter duas casas decimais
c2 = 2345.678
print(f'R${c1:.>28}')
print(f'{p1:.<28}', end=f'R${c2}')
print(f'{p1:.<28}', f'R${c1:.2f}')
print(f'{p1:.<28}', f'R${c1:.2f}')'''

cc11 = 51.1
cc12 = f'R${cc11:.2f}'  #Alterando para sempre ter duas casas decimais
print(f'\n{p1:.<60}', f'{cc12:.>15}')  #Um espaço é adicionado se ficar na mesma linha.

cc21 = 66.649
print(f'\n{p1:.<15}')
'''if len(p1) > 30:  #Tentando criar um limitador de caracteres para o nome do produto
#    p1.replace(p1.index(), '')
for n in range(len(p1)):
    print(n)'''