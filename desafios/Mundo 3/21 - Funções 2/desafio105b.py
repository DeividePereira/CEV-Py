# desafio105.py, mas usando empacotamento
from random import randint


def notas(*n, situation=False):
    """
    Função para analisar notas e situações de um aluno.
    notas(*n, situation='False')
    :param n: as notas do aluno.
    :param situation: opcional, define se aparecerá ou não a situação.
    """
    lista = list()
    dicio = dict()
    for num in n:
        if not str(num) == 'True':
            lista.append(num)

    dicio['total'] = len(lista)
    dicio['maior'] = max(lista)
    dicio['menor'] = min(lista)
    dicio['media'] = sum(lista) / dicio['total']

    if sum(lista) / dicio['total'] >= 5:  # 50% de chance
        dicio['situation'] = 'aprovado'
    else:
        dicio['situation'] = 'reprovado'

    print(f'As notas foram: ', end='')
    for n in lista:
        print(f'{n}', end=' | ')
    print(f'\nForam um total de {dicio["total"]} notas.')
    print(f'A maior nota foi {dicio["maior"]}.')
    print(f'A menor nota foi {dicio["menor"]}.')
    print(f'A média foi {dicio["media"]}.')
    if situation is True:
        print(f'A situação é {dicio["situation"]}.')


notas(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), True)
