"""
* Enumerate - Enumerar elementos da  lista # list
"""
#              0       1       2
#  lista = ['Edu', 'Carlos', 'Ana']


lista = [
    #     0       1       2
    ['Eduardo', 'João', 'Luiz'],  # 0
    ['Edu', 'Jó', 'Lucas'],  # 1
    ['Carla', 'Joana', 'Carlos'],  # 2
]

print(lista[0])
print(lista[1])
print(lista[2])
print('###')
print(lista[1][2])

print('######################')

lista2 = [
    #     0       1       2
    ['Eduarda', 'João', 'Luiza'],  # 0
    ['Eduardo', 'Jóse', 'Luca'],  # 1
    ['Carla', 'Joana', 'Carlos'],  # 2
]
enumerada = enumerate(lista2)
print(enumerada)
print(list(enumerada))

for v1 in enumerate(lista, 53):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2)
