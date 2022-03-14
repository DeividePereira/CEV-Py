import random
from time import sleep
print('Jokenpô contra o computador')
j = str(input('Escolha pedra, papel ou tesoura: ').strip().lower())
c = random.randint(1, 3)
print('PEDRA!')
sleep(1)
print('PA-PEL!')
sleep(1)
print('TESOoouRA!!')
sleep(1)
print('#'*30)
if c == 1:
    print('O computador escolheu pedra.')
    if j == 'pedra':
            print('\033[33mEmpate!\033[m')
    elif j == 'tesoura':
            print('\033[31mDerrota!\033[m')
    else:
            print('\033[32mVitória!\033[m')
elif c == 2:
    print('O computador escolheu papel.')
    if j == 'pedra':
        print('\033[31mDerrota!\033[m')
    elif j == 'tesoura':
        print('\033[32mVitória!\033[m')
    else:
        print('\033[33mEmpate!\033[m')
else:
    print('O computador escolheu tesoura.')
    if j == 'pedra':
            print('\033[32mVitória!\033[m')
    elif j == 'tesoura':
            print('\033[33mEmpate!\033[m')
    else:
            print('\033[31mDerrota!\033[m')
print('#'*30)
