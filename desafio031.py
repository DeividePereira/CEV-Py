""" Preço por passagem
0,50 até 200km, 0,45 viagem mais longas """
d = float(input("Digite a distância, em quilômetros, da viagem: "))
if d > 200:
    print(f"Nesta viajem longa, a passagem é: R${d * 0.45:.2f}")
else:
    print(f"Nesta viajem curta, a passagem é: R${d * 0.50:.2f}")
