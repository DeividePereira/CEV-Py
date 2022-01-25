stud = dict()
stud['name'] = str(input('Insira o nome do(a) estudante: '))

stud['media'] = float((input('Insira a média de notas do(a) estudante: ')))
while stud['media'] < 0 or stud['media'] > 10:
    print('Erro! Tente novamente.')
    stud['media'] = float((input('Insira a média de notas do(a) estudante: ')))
if stud['media'] >= 6:
    stud['status'] = 'aprovado'
else:
    stud['status'] = 'reprovado'

print(f'O(a) aluno(a) {stud["name"]} tem média {stud["media"]}.\nSeu(Sua) estado é {stud["status"]}.')
