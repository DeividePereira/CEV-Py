# Pacote utilidadeCeV, dois módulos internos: moeda e dado
# Transfira todas as funções dos desafios 107, 108 e 109 para o primeiro pacote
# E mantenha tudo funcionando.

from utilidadescev.moeda import resumo
from random import randint

resumo(50.9999, 7, 15)
resumo(randint(2, 1000), randint(1, 100), randint(1, 100))
