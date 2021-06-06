list = list()
while True:
    valor = str(input('Digite um valor: '))
    if not list.count(valor) == 1:  #Checando se o valor é único.
        list.append(valor)

    user = str(input('Você gostaria de continuar?\033[40m[S/N]\033[m')).strip().upper()[0]
    if user == 'N':
        break

print(f'Os valores únicos, em ordem crescente, foram:')
list.sort()
for v in list:
    print(f'{v}', end=' ')