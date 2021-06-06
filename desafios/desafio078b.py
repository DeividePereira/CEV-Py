n = [int(input(f'\nDigite um valor para a posição {pos}: ')) for pos in range(5)]
print(f'\nVocê digitou os valores {n}.')
print(f'\nMaior nº digitado foi {max(n)} nas posições {", ".join(str(i) for i in range(5) if n[i] == max(n))}.')
print(f'Menor nº digitado foi {min(n)} nas posições {", ".join(str(i) for i in range(5) if n[i] == min(n))}.')
