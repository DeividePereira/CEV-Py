# adaptação do desafio070 incompleta.
from time import sleep
counter = 1
while True:
    name = str(input('Name of the product: ')).strip().title()
    if name.isnumeric() or name.isspace():
        print('Invalid value! Try again!')
    else:
        cost = str(input('Cost of the product: US$'))

        if cost.isalpha() or cost.isspace() or cost == '':
            while cost.isalpha() or cost.isspace() or cost == '' or cost:
                print('\033[31mInvalid value! Try again!\033[m')
                cost = str(input('Cost of the product: US$'))
                sleep(0.1)

        user = str(input('Would you like to continue?\033[40m[Y/N]\033[m ')).upper()[0]

        while user != 'Y' and user != "N" or user.isspace() or user == '':
            print('\033[31mInvalid value! Try again!\033[m')
            user = str(input('Would you like to continue?\033[40m[Y/N]\033[m ')).upper()[0]
            if user == 'N':
                break
        if user == 'N':
            break
print('\033[37mProcessing...\033[m')
sleep(0.5)
print('-' * 30)
print(f'')
