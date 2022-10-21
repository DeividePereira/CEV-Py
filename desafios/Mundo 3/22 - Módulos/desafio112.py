# Crie uma função chamada leiaDinheiro() que consiga funcionar como a função input(),
# Mas com uma validação de dados que aceita apenas valores que sejam monetários.

from utilidadescev import dados
from utilidadescev import moeda
from random import randint
from time import sleep

user = dados.leia_dinheiro(1)
moeda.resumo(user, randint(1, 100), randint(1, 100))
sleep(0.3)

user = dados.leia_dinheiro(2.3)
moeda.resumo(user, randint(1, 100), randint(1, 100))
sleep(0.3)

user = dados.leia_dinheiro('4')
moeda.resumo(user, randint(1, 100), randint(1, 100))
sleep(0.3)

user = dados.leia_dinheiro('5.67')
moeda.resumo(user, randint(1, 100), randint(1, 100))
sleep(0.3)

user = dados.leia_dinheiro('8,901')
moeda.resumo(user, randint(1, 100), randint(1, 100))
sleep(0.3)

print('-' * 35)
user = dados.leia_dinheiro(str(input('Digite o preço: R$')))
moeda.resumo(user, randint(1, 100), randint(1, 100))
sleep(0.3)
print('-' * 35)
print('Encerrando...')