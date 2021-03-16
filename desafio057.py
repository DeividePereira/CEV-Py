import time
s = ''
while not s == 'M' or s == 'F':  # Ou while s not in 'MmFf':
    s = str(input('Digite o sexo da pessoa (M ou F): ')).strip().upper()[0]
    if s != 'M' and s != 'F':
        print('\033[31mResposta inválida! Tente novamente!\033[m')
print(f'Sexo {s} registrado com sucesso!')
print('\033[33mFinalizando...\033[m')
time.sleep(1)
