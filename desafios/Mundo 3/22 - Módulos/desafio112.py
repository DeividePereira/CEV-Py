# Crie uma função chamada leiaDinheiro() que consiga funcionar como a função input(),
# Mas com uma validação de dados que aceita apenas valores que sejam monetários.

from utilidadescev import dados
from utilidadescev import moeda
from random import randint
from time import sleep

testes = (1, 2.3, '5.67', '8,901', str(input('Digite o preço: R$')))
print('-' * 25)
for cada_teste in testes:
    user = dados.leia_dinheiro(cada_teste)
    moeda.resumo(user, randint(1, 100), randint(1, 100))
    sleep(1.25)
    print('-' * 25)

print('Encerrando...')
sleep(1.25)
