# Módulo moeda.py que tenha as funções: aumentar() em %, diminuir() em %, dobro() e metade()
# Programa que importe esse módulo e use algumas dessas funções.

from utilidadescev import moeda

user = float(input('Digite o preço: R$'))
print(f'A metade de {user} é {moeda.metade(user)}')
print(f'O dobro de {user} é {moeda.dobro(user)}')
print(f'Aumentando 12% fica {moeda.aumentar(user, 12)}')
print(f'Reduzindo 7% fica {moeda.diminuir(user, 7)}')
