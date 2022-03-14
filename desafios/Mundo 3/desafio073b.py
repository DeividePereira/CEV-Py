FWei = ('Gary Russell Jr', 'Rey Vargas', 'Tugstsogt Nyambayar', 'Lerato Dlamini', 'Mauricio Lara', 'Mark Magsayo',
        'Kid Galahad', 'Josh Warrington', 'Joet Gonzalez', 'Hinata Maruta', 'Isaac Lowe', 'Julio Ceja',
        'Isaac Dogboe', 'Andoni Gago', 'Satoshi Shimizu', 'Dennis Contreras')
print(f'\033[33mOs primeiros cinco colocados são:\033[m\n{FWei[0:6]}')
print(f'\033[31mOs últimos cinco colocados são:\033[m\n{FWei[-5:]}')
print(f'\033[33mO ranking em ordem alfabética é:\033[m\n{sorted(FWei)}')
user = input(str('Digite um nome da lista: ')).strip().title()
if user == 'Gary Russell Jr':
    print(f'{user} é o Campeão.')
else:
    print(f'{user} está na {FWei.index(user)}° posição.')
