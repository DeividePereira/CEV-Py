""" Número; Se é par ou ímpar.
n % 2 = 0 -> par
n % 3 = 0 -> ímpar """
# Obs de Erro!: Usando n % 3 -> n = 1 -> "n é par".
# Obs. 2: n = 0 -> "n é ímpar".
n = int(input("Digite um número inteiro: "))
if n % 2 == 0:
    print("Esse número é par.")
else:
    print("Esse número é ímpar.")
