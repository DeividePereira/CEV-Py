nome = str(input(f'Digite o nome completo: ').strip())
print(f'O nome todo em maiúsculo fica: {nome.upper()}')
print(f'O nome todo em minúsculo fica: {nome.lower()}')
print(f'O nome todo sem espaços tem: {len(nome) - nome.count(" ")}')
separado = nome.split()
print(f'O primeiro nome tem: {len(separado[0])} letras.')
