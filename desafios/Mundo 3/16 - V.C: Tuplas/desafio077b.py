conjunto = ('python', 'futuro', 'programar', 'humano', 'escassez', 'quadruplo', 'afago', 'convexo', 'desinteressante',
            'passagem', 'abismo', 'pena', 'carteiro', 'rosario', 'falho', 'observador', 'ameba', 'besta', 'girassol',
            'amigo', 'fumo', 'absurdamente', 'alce', 'ladra', 'ornitorrinco', 'convincente', 'arriscado', 'destruído',
            'carapaça', 'película',)
numletra = 0
#há um loop for para cada palavra da tupla, e um loop para cada letra de cada palavra da tupla.
for palavra in conjunto:  #erro: o numletra se acumula pelas diferentes palavras.

    if numletra == 0:
        print(f'\nA palavra \033[31m{palavra}\033[m não tem vogais.', end='')
    elif numletra == 1:
        print(f'\nA palavra \033[33m{palavra}\033[m tem a vogal: ', end='')
    else:
        print(f'\nA palavra \033[36m{palavra}\033[m tem as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'a á ã â e é ê i í o ó õ u ú':
            print(letra, end=' ')
