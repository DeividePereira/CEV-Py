palavras = ('python', 'futuro', 'programar', 'humano', 'escassez', 'quadruplo', 'afago', 'convexo', 'desinteressante',
            'passagem', 'abismo', 'pena', 'carteiro', 'rosario', 'falho', 'observador', 'ameba', 'besta', 'girassol',
            'amigo', 'fumo', 'absurdamente', 'alce', 'ladra', 'ornitorrinco', 'convincente')
numletra = 0
for p in palavras:
    print(f'\nA palavra \033[36m{p}\033[m tem as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            numletra += 1
