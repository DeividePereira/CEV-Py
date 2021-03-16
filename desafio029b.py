"""" v > 80km/h -> multa
multa: R$7.00 por cada km acima do limite """
v = int(input('Digite a velocidade do carro no momento que passou no radar: '))
if v > 80:
    print(f"A multa é R${(v-80) * 7}.")
print("Não foi multado.")
# Condição simples
