# Adicione ao moeda.py, o resumo(), que mostra na tela em uma tabela algumas informações
# Geradas pelas funções que já temos nos módulos criados até aqui.

from utilidadescev.moeda import resumo
from random import randint

resumo(50.9999, 7, 15)
resumo(randint(2, 1000), randint(1, 100), randint(1, 100))
