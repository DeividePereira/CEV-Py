# criar uma lista mega_sena, colocar sub-listas 'jogos' dentro de mega_sena. o usuário deve definir quantos jogos;
# 6 números entre 0 a 60
from random import randint
nome = 'Mega Sena Ant\'s Harpoon'
mega_sena = list()
jogo = list()
user = int(input('Insira quantos jogos de mega sena deseja: '))
print('=-=' * 16)
for a in range(0, user):        #Número de jogos
    for b in range(0, 6):       #Cada jogo deve ter 6 números.
        jogo.append((randint(0, 60)))
        mega_sena.append(jogo[:])
    print(f'Jogo n°{a + 1}: {jogo}')
    jogo.clear()
