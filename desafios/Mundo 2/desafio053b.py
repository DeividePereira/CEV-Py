x = str(input("Digite uma palavra/frase: ")).strip().upper()

print(f"O contrário de {x.replace(' ', '')} é {x[::-1].replace(' ', '')}")

print("É palíndromo!" if x[::].replace(' ', '') == x[::-1].replace(' ', '') else "Não é palíndromo!")