from time import sleep
total = morett = cheapest = name_cheapest = 0
counter = 1
while True:
    print('==-==-==-==-==-==-==-==-==-==')
    print(f'\033[34mProduct Number {counter}\033[m')
#    print(f'==-==-==-==-==-==-==-==-==-==\n\033[34m{"Cadastro de Pessoas":^29}\033[m\n==-==-==-==-==-==-==-==-==-==')

    name = str(input('Name of the product: ')).strip().title()
    if name.isnumeric() or name.isspace():
        while name.isnumeric() or name.isspace():
            print('Invalid value! Try again!')
            name = str(input('Name of the product: ')).strip().title()
    else:
        cost = str(input('Cost of the product: US$'))

        if cost.isalpha() or cost.isspace() or cost == '':
            while cost.isalpha() or cost.isspace() or cost == '' or cost:
                print('\033[31mInvalid value! Try again!\033[m')
                cost = str(input('Cost of the product: US$'))
                sleep(0.1)

        if float(cost) > 1000:
            morett += 1

        if counter == 1:
            name_cheapest = name
            cheapest = float(cost)

        else:
            if cheapest > float(cost):
                cheapest = float(cost)
                name_cheapest = name

        total += float(cost)
        cont = str(input('Would you like to continue?\033[40m[Y/N]\033[m ')).upper()[0]

        while cont != 'Y' and cont != "N" or cont.isspace() or cont == '':
            print('\033[31mInvalid value! Try again!\033[m')
            cont = str(input('Would you like to continue?\033[40m[Y/N]\033[m ')).upper()[0]

            if cont == 'N':
                break
        if cont == 'N':
            break

        if cont == 'Y':
            counter += 1
print('\033[37mProcessing...\033[m')
sleep(0.5)
print('==-==-==-==-==-==-==-==-==-==')
print(f'The total is US${total:.2f}')
print(f'There are {morett} products that costs more than US$1000.00')
print(f'The cheapest product is the {name_cheapest} that costs US${cheapest:.2f}')
