def voto(nascimento):
    from datetime import date
    idade = date.today().year - nascimento
    if 16 <= idade < 18 or 65 <= idade < 120:
        print(f'Estado do voto com {idade} anos: opcional.')

    elif 18 <= idade < 65:
        print(f'Estado do voto com {idade} anos: obrigatório.')

    elif 0 <= idade < 16:
        print(f'Estado do voto com {idade} anos: negado.')

    else:
        print(f'    \033[31mErro! Você teria {idade} anos. Tente novamente.\033[m')
        voto(int(input('Qual é o seu ano de nascimento? ')))  # Uma tentativa


voto(int(input('Qual é o seu ano de nascimento? ')))
