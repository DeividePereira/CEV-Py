garota = ma = soma = ivelho = nvelho = 0
p = int(input('Quantas pessoas deseja analisar? '))

for perfil in range(1, p+1, 1):
    print(f'----- {perfil}ª pessoa ----- ')
    n = str(input('Nome: ')).strip().title()
    i = int(input('Idade: '))
    s = str(input('Sexo(M ou F): ')).strip().upper()
    soma += i
    ma = soma/p

    if s != 'M' and s != 'F':
        print('Resposta inválida!')
        exit()

    if s == 'M' and i > ivelho:
        ivelho = i
        nvelho = n

    if s == 'F' and i < 20:
        garota += 1

print(f'A média de idade da amostra é de {ma:.1f} anos.')
print(f'O homem mais velho é o {nvelho} e tem {ivelho} anos.')
print(f'No total, há {garota} pessoas do sexo feminino com menos de 20 anos.')
