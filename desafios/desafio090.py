stud = dict()
stud['name'] = str(input('Insira o nome do(a) estudante: ').title())

stud['media'] = float((input('Insira a média de notas do(a) estudante: ')))
while stud['media'] < 0 or stud['media'] > 10:
    print('Erro! Tente novamente.')
    stud['media'] = float((input('Insira a média de notas do(a) estudante: ')))
if stud['media'] >= 6:
    stud['status'] = 'aprovado(a)'
else:
    stud['status'] = 'reprovado(a)'
print('-=' * 23)
print(f' - O(a) aluno(a) {stud["name"]};\n - Tem média {stud["media"]};\n - Seu estado é {stud["status"]}.')
