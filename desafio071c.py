""""(1)Versão com o for"""

lista = [100, 50, 20, 10, 5, 2, 1]
valor = int(input('Insira o valor que desaja sacar R$ '))
for n in range(len(lista)):
    if valor >= lista[n]:
        nota = valor // lista[n]
        print(f'\033[31mTotal de {nota} notas de R$ {lista[n]}')
        valor = valor % lista[n]
print('\n\033[34mVolte sempre ao Banco do Cev! Tenha um bom dia!')