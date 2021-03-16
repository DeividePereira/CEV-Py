import random
a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))
classe = [a, b, c, d]
print(f'Quem deverá apagar o quadro é: {random.choice(classe)}')
