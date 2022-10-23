def metade(user, form=True):
    user = str(user).replace(',', '.')
    user = float(user)

    user /= 2
    return dinheiro(user) if form is True else user


def dobro(user, form=True):
    user = str(user).replace(',', '.')
    user = float(user)

    user *= 2
    return dinheiro(user) if form is True else user


def aumentar(user, p=10, form=True):
    user = str(user).replace(',', '.')
    user = float(user)

    user = user + user * (p / 100)
    return dinheiro(user) if form is True else user


def diminuir(user, p=10, form=True):
    user = str(user).replace(',', '.')
    user = float(user)

    user = user - user * (p / 100)
    return dinheiro(user) if form is True else user


def dinheiro(user):
    # Essa função está incluída nas outras.
    user = str(user).replace(',', '.')
    user = float(user)
    return f'R${user:.2f}'.replace(".", ",")


def resumo(user, p_mais=10, p_menos=10):
    print(f'{user} / 2   = {metade(user, True)}'
          f'\n{user} * 2   = {dobro(user, True)}'
          f'\n{user} + {p_mais}% = {aumentar(user, p_mais, True)}'
          f'\n{user} - {p_menos}% = {diminuir(user, p_menos, True)}')
