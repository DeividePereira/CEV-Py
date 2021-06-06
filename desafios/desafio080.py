# 5 valores, ordene-os sem usar .sort
list = list()
cont = first = 0
for n in range(0, 6):
    user = int(input('Digite um número natural: '))
    cont += 1
    if cont == 1:
        list.append(user)
        first = 1
    if cont > 1 and user < first:
        list.insert(first, user)
    else:
        list.insert(user, first)
print(list)
print(first)
