from random import randint


def notas(a, b, c, d, situation=False):
    """
    Função para analisar notas e situações de um aluno.
    notas(a,b,c,d, situation='False')
    :param a: primeira nota.
    :param b: segunda nota.
    :param c: terceira nota.
    :param d: quarta nota.
    :param situation: opcional, define se aparecerá ou não a situação.
    """
    lista = list()
    dicio = dict()
    lista.append(a)
    lista.append(b)
    lista.append(c)
    lista.append(d)

    dicio['total'] = len(lista)
    dicio['maior'] = max(lista)
    dicio['menor'] = min(lista)
    dicio['media'] = sum(lista) / dicio['total']

    if sum(lista) / dicio['total'] >= 6:
        dicio['situation'] = 'aprovado'
    else:
        dicio['situation'] = 'reprovado'

    print(f'As notas foram: ', end='')
    for n in lista:
        print(f'{n}', end=' | ')
    print('')
    print(f'Foram um total de {dicio["total"]} notas.')
    print(f'A maior nota foi {dicio["maior"]}.')
    print(f'A menor nota foi {dicio["menor"]}.')
    print(f'A média foi {dicio["media"]}.')
    if situation is True:
        print(f'A situação é {dicio["situation"]}.')


notas(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), True)
