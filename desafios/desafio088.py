from random import randint
from time import sleep
nome = 'Mega Sena Ant\'s Harpoon'
mega_sena = list()
jogo = list()
j = 0
print(f'=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=\n\033[36m{nome:^48}\033[m'
      f'\n=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=')
user = int(input('Insira quantos jogos de mega sena deseja: '))
while user <= 0:
    print('\033[31mValor Inválido! Tente novamente.\033[m')
    user = int(input('Insira quantos jogos de mega sena deseja: '))
print(f'=-=-=-=-=-=-=-\033[36m Sorteando {user} jogos\033[m -=-=-=-=-=-=-=')

'''           Requisitos:
 Deve haver 'user' número de jogos;
 Cada jogo deve haver 6 números;
 Cada número deve variar de 1 a 60, sem repetir.
           Planejamento:
 'mega_sena' é o agrupamento de todos os jogos;
 'jogo' é um dos 'user' grupos de números;
 'j' é a contagem de número de jogos;
 'num' é cada número de 'jogo';
 'n' é a contagem de números de cada 'jogo' '''

while len(mega_sena) != user:
    while len(jogo) != 6:       #Contagem da quantidade de números.
        num = randint(1, 60)    #Números de 1 a 60.
        if num not in jogo:
            jogo.append(num)
            jogo.sort()
    j += 1                      #Contagem do número de jogos
    sleep(0.25)
    print(f'Jogo n°{j}: {jogo}')
    mega_sena.append(jogo[:])
    jogo.clear()
print(f'=-=-=-=-=-=-=-=-=-\033[36m Boa sorte!\033[m -=-=-=-=-=-=-=-=-=')
