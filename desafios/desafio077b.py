palavras = ('python', 'futuro', 'programar')
print(palavras[0])
for c in palavras[0]:
    if c == 'a' or 'e' or 'i' or 'o' or 'u':
        print(f'{c}', end=' ')
        #print(f'{palavras[0].index(c)}')
