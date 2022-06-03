"""
Funções lambda
"""


# a = lambda x, y: x * y
# print(a(2,2))

lista = [
    ['P1', 13],
    ['P2', 10],
    ['P3', 19],
    ['P4', 8],
    ['P5', 5],
]


# lista.sort(key=lambda item: item[1], reverse=True)

print(sorted(lista, key=lambda i: i[1]))
print(lista)
