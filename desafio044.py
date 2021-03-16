from time import sleep
v = float(input('Digite o valor do produto: R$'))
print('\033[40m[1]\033[m - Para dinheiro/cheque\n\033[40m[2]\033[m - Para cartão')
c = int(input('Escolha a condição de pagamento: '))
while c != 1 and c != 2:
    print('\033[31mOpção inválida! Tente novamente.\033[m')
    sleep(0.5)
    c = int(input('Escolha a condição de pagamento: '))
if c == 1:
    print(f'Em dinheiro e cheque, damos 10% de desconto.\nPortanto, o valor final é R${v - v * (10/100):.2f}')
elif c == 2:
    m = int(input('Digite em quantas vezes pagará: '))
    if m == 1:
        print(f'Oferecemos 5% de desconto. O valor final é R${v - v * (5/100):.2f}')
    elif m == 2:
        print(f'Não oferecemos desconto. O valor do produto é R${v:.2f}')
        print(f'A parcela mensal fica R${v/m}')
    else:
        print(f'O valor do produto é R${v:.2f} com 20% de juros.')
        print(f'A parcela mensal é R${v/m:.2f}')
