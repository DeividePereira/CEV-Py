from time import sleep
dic = dict()
l_gols = list()
goltotal = 0
dic['nome'] = str(input('Insira o nome do(a) jogador(a): ')).title()
while len(dic['nome']) == 0:
    print('Erro! Tente novamente.')
    dic['nome'] = str(input('Insira o nome do(a) jogador(a): ')).title()
qtpartidas = int(input('Quantas partidas ele(a) jogou? '))
for p in range(1, qtpartidas + 1):
    gol = int(input(f'Quantos gols ele(a) fez na {p}ª partida? '))
    l_gols.append(gol)
    goltotal += gol     #somatório
dic['gols'] = l_gols.copy()
dic['gtotal'] = goltotal

print('-=' * 20)
print(f'O(A) jogador(a) {dic["nome"]} jogou {qtpartidas} partidas.')
for n in range(1 , qtpartidas + 1):
    print(f'   Na {n}ª partida, fez {l_gols[n-1]} gols.')
print(f'Totalizando {dic["gtotal"]} gols.')