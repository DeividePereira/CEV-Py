# desafio107.py, acrescentar um parâmetro. Informando se o valor retornado...
# por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio108.py

from utilidadescev import moeda

user = float(input('Digite o preço: R$'))
print('-' * 30)
print(f'A metade de {user} é {moeda.metade(user)}')
print(f'O dobro de {user} é {moeda.dobro(user, False)}')
print(f'Aumentando 12% fica {moeda.aumentar(user, 12, False)}')
print(f'Reduzindo 7% fica {moeda.diminuir(user, 7, True)}')
