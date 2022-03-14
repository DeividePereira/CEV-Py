# Copiado dos comentários do vídeo. E levemente melhorado.
a = int(input('digite um valor '))
b = int(input('digite um valor '))
c = int(input('digite um valor '))
if a == b and b == c:
    print('Haha! Todos os números sao iguais.')
else:
    if a > b and a > c:
        print('Dentre o número {}, {} e {}, o maior número é {}.'.format(a, b, c, a))
    else:
        if b > a and b > c:
            print('dentre os números {}, {} e {}, o maior número é {} '.format(a, b, c, b))
        else:
            print('dentre todos os números {}, {} e  {}  é o maior deles é {}'.format(a, b, c, c))
