'''Melhore o desafio093, para que funcione com vários jogadores.
Incluia um sistema de vizualização de 'detalhes do aproveitamento' de cada jogador.'''
from time import sleep
dicio = dict()      #dicio = {'nome' = 'abcw', 'qtpartidas' = 4, 'gols' = [1,2,3,4], 'gtotal' = 10}
l_dicios = list()
l_gols = list()
gtotal = 0
contador = gg = 1
while True:

    dicio['nome'] = str(input(f'Insira o nome do(a) {contador}º jogador(a): ')).title()
    while len(dicio['nome']) == 0:
        print('Erro! Tente novamente.')
        dicio['nome'] = str(input(f'Insira o nome do(a) {contador}º jogador(a): ')).title()
    
    dicio['qtpartidas'] = int(input('Quantas partidas ele(a) jogou? '))
    while dicio['qtpartidas'] <= 0:
        print('Erro! Tente novamente. Não pode ser menor que 1.')
        dicio['qtpartidas'] = int(input('Quantas partidas ele(a) jogou? '))
    
    for p in range(1, dicio['qtpartidas'] + 1):
        gol = int(input(f'Quantos gols ele(a) fez na {p}ª partida? '))
        l_gols.append(gol)
        gtotal += gol
    dicio['gols'] = l_gols.copy()
    dicio['gtotal'] = gtotal

    continuar = str(input('  Deseja acrescentar jogadores?\033[40m[S/N]\033[m ')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        print('    Erro! Tente novamente.')
        continuar = str(input('  Deseja acrescentar jogadores?\033[40m[S/N]\033[m ')).strip().upper()[0]
    l_dicios.append(dicio.copy())
    dicio.clear()
    l_gols.clear()
    if continuar == 'N':
        break
    else:
        contador += 1

p1 = 'Código'
p2 = 'Nome'
p3 = 'Número de partidas'
p4 = 'Gols totais'
while True:
    print('\n=---------------= Tabela dos jogadores =---------------=')
    print(f'{p1:^6} | {p2:^10} | {p3:^18} | {p4:^4}')
    for a in range(0, contador):
        print(f'''{a + 1:^6} | {l_dicios[a]["nome"]:^10} | {l_dicios[a]["qtpartidas"]:^18} | {l_dicios[a]["gtotal"]:^11}''')

    code = int(input('\nDigite um dos códigos para ver detalhes\033[40m[0 para nenhum]\033[m: '))
    while not -1 < code <= contador:
        print('    Erro! Tente novamente.')
        code = int(input('Digite um dos códigos para ver detalhes\033[40m[0 para nenhum]\033[m: '))
    if code == '0':
        break
    else:
        print(f'=---------------= Detalhamento dos jogadores =---------------=') #Detalhamento dos jogadores
        # código começa em 1, mas dicio começa em 0; code - 1 = código
        print(f'Gols do(a) jogador(a) {l_dicios[code - 1]["nome"]}')
        for g in l_dicios[code - 1]["gols"]:
            print(f'      No {gg}º jogo: {g} gols')
            gg += 1
        gg = 1

        cont = str(input('  Deseja continuar?\033[40m[S/N]\033[m')).strip().upper()[0]
        while cont != 'S' and cont != 'N':
            print('    Erro! Tente novamente.')
            cont = str(input('  Deseja continuar?\033[40m[S/N]\033[m')).strip().upper()[0]
        if cont == 'N':
            break
print('\nEncerrando...')