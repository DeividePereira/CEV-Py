# Adapte o desafio107.py, crie uma função moeda() que mostra os valores como valor monetário formatado.
# Ao invés de 12.95, mostre: R$12,95.
from utilidadescev import moeda

user = float(input('Digite o preço: R$'))
print(f'A metade de {user} é {moeda.dinheiro(moeda.metade(user))}')
print(f'O dobro de {user} é {(moeda.dinheiro(moeda.dobro(user)))}')
print(f'Aumentando 12% fica {moeda.dinheiro(moeda.aumentar(user, 12))}')
print(f'Reduzindo 7% fica {moeda.dinheiro(moeda.diminuir(user, 7))}')
