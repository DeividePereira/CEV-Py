list = list()  #versão complexa do desafio079, incompleta
while True:
    valor = str(input('Digite um valor: '))
    while not valor.isnumeric:
        valor = str(input('Digite um valor: '))
    if not list.count('valor') == 1:
        list.append(valor)

    user = str(input('Você gostaria de continuar?\033[40m[S/N]\033[m')).strip().upper()[0]
    if user != 'S' and 'N':
        while user != 'S' and 'N':
            user = str(input('Você gostaria de continuar?\033[40m[S/N]\033[m')).strip().upper()[0]
        if user == 'N':
            break
    if user == 'N':
        break

print(f'Os valores únicos, em ordem crescente, foram: \n')
list.sort()
for v in list:
    print(f'{v}', end=' ')
# 1- checar se valor está em número
# 2- se for número, passar para o próximo passo com ELSE?!
