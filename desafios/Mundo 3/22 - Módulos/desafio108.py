# Adapte o desafio107.py, crie uma função moeda() que mostra os valores como valor monetário formatado. 12.95 -> 12,95.
from utilidadescev import moeda

user = float(input('Digite o preço: R$'))  # Editado, precisa do False.
print(f'A metade de {user} é {moeda.dinheiro(moeda.metade(user, False))}')
print(f'O dobro de {user} é {moeda.dinheiro(moeda.dobro(user, False))}')
print(f'Aumentando 12% fica {moeda.dinheiro(moeda.aumentar(user, 12, False))}')
print(f'Reduzindo 7% fica {moeda.dinheiro(moeda.diminuir(user, 7, False))}')
