""" 1 - Verificar se uma variável = '   '.strip == '' -> True!

"""

v1 = str(input('Por favor, funciona: ')).strip()
print(f'\033[40m{v1}\033[m')
print(len(v1))  # Resultado: 0 caractéres, remove todos os espaços. Então é True!
