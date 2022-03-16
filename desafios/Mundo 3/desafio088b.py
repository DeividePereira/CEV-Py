# Os números podem repetir.
from random import randint
from time import sleep
nome = 'Sorteio Ant\'s Harpoon'
jogo = list()
print(f'=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=\n\033[36m{nome:^48}\033[m'
      f'\n=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=')
user = int(input('Insira quantos jogos de sorteio deseja: '))
print(f'=-=-=-=-=-=-=- Sorteando {user} jogos -=-=-=-=-=-=-=')

for a in range(0, user):        #Número de jogos
    for b in range(0, 6):       #Cada jogo deve ter 6 números.
        jogo.append(randint(0, 60))
    print(f'Jogo n°{a + 1}: {sorted(jogo)}')
    sleep(0.25)
    jogo.clear()
print('Boa sorte!')
