def ficha(nome='<desconhecido', gols='0'):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0

    print('-' * 52)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-' * 50)
ficha(str(input('Nome do jogador: ').strip().title()), str(input('Número de gols: ').strip()))
