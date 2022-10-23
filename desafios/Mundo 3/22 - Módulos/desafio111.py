# Crie o pacote utilidadeCeV, e dois módulos internos: moeda e dado.
# Transfira todas as funções dos desafios 107, 108 e 109 para moeda.
# /// A seguir, apenas testes.
from utilidadescev.moeda import resumo
from random import randint

print('-' * 25)
resumo(100)
print('-' * 25)
resumo(50.9999, 7, 15)
print('-' * 25)
resumo(randint(2, 1000), randint(1, 100), randint(1, 100))
