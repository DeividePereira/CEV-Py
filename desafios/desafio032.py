""" Este ano é bissexto? """
a = int(input('Digite um ano: '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('Esse ano é bissexto: ')
else:
    print('Esse ano não é bissexto.')
