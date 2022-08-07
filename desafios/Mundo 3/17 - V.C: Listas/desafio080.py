list = list()
for n in range(1, 6):
    user = int(input('Digite um número natural: '))
    if n == 1 or user >= max(list):
        list.append(user)
        print(f'Adicionado ao final da lista.')
        print(list)
    else:
        posi = 0
        while posi < len(list):
            if user <= list[posi]:
                list.insert(posi, user)
                print(f'Adicionado na {posi + 1}° posição.')
                break
            posi += 1
        print(list)
print(f'A lista resultante é: {list}')
