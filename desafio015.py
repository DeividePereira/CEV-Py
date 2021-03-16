km = int(input('A quantidade de quilômetros rodados foi: '))
dias = int(input('O carro foi alugado por quantos dias? '))
print(f'O valor a ser pago é: R${((km*0.15)+(dias*60)):.2f}')
