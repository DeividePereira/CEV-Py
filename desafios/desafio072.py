num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
       'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
user = int(input('Digite um número cardinal entre 0 e 20: '))
print(f'Você digitou o número \033[36m{num[user]}\033[m.')
