"""
Desempacotamento de listas em Python
"""
lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n1, n2, *outra_lista, ultimo_da_lista = lista

print(n2, outra_lista, ultimo_da_lista)
print(outra_lista)
