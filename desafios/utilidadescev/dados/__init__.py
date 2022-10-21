def leia_dinheiro(user):
    user = str(user).strip()
    special_characters = '!@#$%^&*()?_=<>/'
    while True:
        check = 0
        letters = 0

        if user == '' or user.count(' ') > 0:
            print(f'{user} | \033[31mInválido\033[m | Razão: Espaço')
        else:
            check += 1

        for char in user:
            if char.isalpha():
                letters += 1
        if letters != 0:
            print(f'{user} | \033[31mInválido\033[m | Razão: {letters} letras')
        else:
            check += 1

        if not user.isascii():
            print(f'{user} | \033[31mInválido\033[m | Razão: Não-ASCII')
        else:
            check += 1

        if user.count(',') > 1 or user.count('.') > 1 or user.count(',') + user.count('.') > 1:
            print(f'{user} | \033[31mInválido\033[m | Razão: Quantidade de . ou ,')
        else:
            check += 1

        if user.find('-') >= 1:
            print(f'{user} | \033[31mInválido\033[m | Razão: Posição do -')
        else:
            check += 1

        if user.count('-') != 0 and user.count('-') != 1:
            print(f'{user} | \033[31mInválido\033[m | Razão: Quantidade de -')
        else:
            check += 1

        if any(c in special_characters for c in user):
            print(f'{user} | \033[31mInválido\033[m | Razão: Caracteres Especiais')
        else:
            check += 1

        if check == 7:
            user = user.replace(',', '.')
            return user
        else:
            print('-' * 20)
            user = str(input('Digite o preço: R$'))
