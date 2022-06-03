"""
For / Else em Python
"""

"""
lista = ['Maçã', 'Abacate', 'batata']

for valor in lista:
    if valor.startswith('A'):
        print('Começa com "A"', valor)
    else:
        print('Não começa com "A"', valor)
"""
lista = ['Maçã', 'Abacate', 'Batata', 'João']

comeca_j = False
for valor in lista:
    if valor.lower().startswith('j'):
        continue
      # comeca_j = True
    print(valor)
#  if comeca_j:
#    print('Existe uma palavra que começa com J.')
#  else:
#    print('Não existe uma palavra que começa com J.')
