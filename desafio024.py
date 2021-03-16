"""Verificar se a cidade começa com a palavra Santo"""
c = str(input('Digite o nome de uma cidade: ').strip().capitalize())
u = c.split()
print(f'Essa cidade começa com a palavra Santo? {"Santo" in u}')
