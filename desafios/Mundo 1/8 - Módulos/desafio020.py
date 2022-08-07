import random
a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))
ordem = [a, b, c, d]
random.shuffle(ordem)
print(f'A ordem de quem deverá apagar o quadro é: {ordem}')
