def metade(user, form=False):
    if form is True:
        user /= 2
        return f'R${user:.2f}'.replace(".", ",")
    else:
        user /= 2
        return user


def dobro(user, form=False):
    if form is True:
        user *= 2
        return f'R${user:.2f}'.replace(".", ",")
    else:
        user *= 2
        return user


def aumentar(user, p=10, form=False):
    if form is True:
        user = user + user * (p / 100)
        return f'R${user:.2f}'.replace(".", ",")
    else:
        user = user + user * (p / 100)
        return user


def diminuir(user, p=10, form=False):
    if form is True:
        user = user - user * (p / 100)
        return f'R${user:.2f}'.replace(".", ",")
    else:
        user = user - user * (p / 100)
        return user


def dinheiro(user):  # Essa função está embutida nas outras.
    return f'R${user:.2f}'.replace(".", ",")


def resumo(user, p_mais=10, p_menos=10):
    half = user / 2
    half = f'R${half:.2f}'.replace(".", ",")

    double = user * 2
    double = f'R${double:.2f}'.replace(".", ",")

    increase = user + user * (p_mais / 100)
    increase = f'R${increase:.2f}'.replace(".", ",")

    decrease = user - user * (p_menos / 100)
    decrease = f'R${decrease:.2f}'.replace(".", ",")

    print('-' * 35)
    print(f'{user} / 2   = {half}'
          f'\n{user} * 2   = {double}'
          f'\n{user} + {p_mais}% = {increase}'
          f'\n{user} - {p_menos}% = {decrease}')


# Testes a seguir:
# print(metade(50))
# print(dobro(50))
# print(aumentar(50, 10))  # 55
# print(diminuir(50, 10))  # 45
# print(dinheiro(5))
# print(dinheiro(5.5))
# resumo(100)
# resumo(50.9999, 7, 15)
