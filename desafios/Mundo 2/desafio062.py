"""Feito pelo Prof. Guanabara"""
a = int(input('Qual o termo inicial? '))
r = int(input('Qual a razão? '))
t = a
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= 10:
        print(f'{t}', end=" → ")
        t += r
        cont += 1
    print(f'Pausa! {cont - 1} termos!')

    mais = int(input('Deseja exibir mais quantos termos? \n(Digite 0 Para finalizar)'))

print(f'Foram exibidos {total} termos.')
