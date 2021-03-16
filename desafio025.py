"""Verificar se a cidade tem a palavra Santo"""
c = str(input('Digite o nome de uma cidade: ').strip().title())
print(f'Essa cidade tem a palavra Santo? {"Santo" in c}')
