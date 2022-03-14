num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
       'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    user = int(input('Digite um número cardinal entre 0 e 20: '))
    if user < 0 or user > 20:
        print('\033[31mO número digitado está fora do limite!\033[m')
    else:
        break
print(f'Você digitou o número \033[36m{num[user]}\033[m.')
