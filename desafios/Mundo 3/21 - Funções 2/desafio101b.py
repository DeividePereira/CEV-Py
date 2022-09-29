def voto2(nascimento):
    from datetime import date
    idade = date.today().year - nascimento

    # Tratamento de erro
    while not date.today().year > nascimento > (date.today().year - 140):
        print(f'    \033[31mErro! Você teria {idade} anos. Tente novamente.\033[m')
        nascimento = int(input('Qual é o seu ano de nascimento? '))
        idade = date.today().year - nascimento

    idade = date.today().year - nascimento
    if 16 <= idade < 18 or 65 <= idade < 140:
        return f'Estado do voto com {idade} anos: opcional.'

    elif 18 <= idade < 65:
        return f'Estado do voto com {idade} anos: obrigatório.'

    elif 0 <= idade < 16:
        return f'Estado do voto com {idade} anos: negado.'


print(voto2(2004))
print('-' * 40)
print(voto2(int(input('Qual é o seu ano de nascimento? '))))
