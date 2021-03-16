n1 = float(input('Digite a nota da avaliação 1: '))
n2 = float(input('Digite a nova da avaliação 2: '))
m = (n1 + n2) / 2
if m >= 7:
    print('Aprovado!')
elif 7 > m >= 5:
    print('Recuperação!')
else:
    print('Reprovado!')
