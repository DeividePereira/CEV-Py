val = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite seu salário: R$'))
anos = float(input('Digite em quantos anos pagará: '))
parc = anos * 12
valmen = val / parc
if valmen > sal * (30/100):
    print('O empréstimo não pode ser realizado por exceder o limite.')
    print('Caso seja possível, aumente o período de pagamento ou o salário.')
else:
    print('O empréstimo foi realizado com sucesso.')
    print(f'A casa de valor R${val:.2f} deverá ser quitada em {anos:.0f} anos. No valor mensal de R${valmen:.2f}')
