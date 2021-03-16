f = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra "o" aparece {f.count("o")} vezes')
print(f'A primeira letra "o" aparece na posição: {f.find("o")+1}')
print(f'A última letra "o" aparece na posição: {f.rfind("o")+1}')
