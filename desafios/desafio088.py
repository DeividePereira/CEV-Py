from random import randint
from time import sleep
nome = 'Mega Sena Ant\'s Harpoon'
mega_sena = list()
jogo = list()
print(f'=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=\n\033[36m{nome:^48}\033[m'
      f'\n=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=')
user = int(input('Insira quantos jogos de mega sena deseja: '))
print(f'=-=-=-=-=-=-=- Sorteando {user} jogos -=-=-=-=-=-=-=')

'''for a in range(0, user):        #Número de jogos
    for b in range(0, 6):       #Cada jogo deve ter 6 números.
        jogo.append((randint(1, 60)))   #Cada número vai de 1 a 60
        mega_sena.append(jogo.sort()[:])
    print(f'Jogo n°{a + 1}: {jogo}')
    sleep(0.25)
    jogo.clear()'''

for a in range(0, user):        #Número de jogos
    for b in range(0, 6):
        num = randint(1, 6)
        if num not in jogo:
            jogo.append(num)
            b += 1
    print(f'Jogo n°{a + 1}: {sorted(jogo)}')
    sleep(0.25)
    jogo.clear()
print('Boa sorte!')
