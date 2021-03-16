from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento').strip())
i = atual - nasc
print(f'Quem nasceu em {nasc} tem {i} anos em {atual}.')
