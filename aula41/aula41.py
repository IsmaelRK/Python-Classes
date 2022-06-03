# Tuplas não podem ser alteradas a não ser que sejam convertidas em listas com "t1 = list(t1)"

t1 = 1, 2, 'batata'
t1 = list(t1)
t1[1] = 3  # Tupla convertida em lista e alterada
print(t1)
t1 = tuple(t1)  # E volta a ser tupla

# t2 = 3, 4, 56, 98
#
# try:
#     t2[0] = 'cinco'
# except:
#     print('Não Permitido')


# t = (1, 2, 3, 94) * 2
# print(t)

# t1 = 1, 2, 'batata'
# t2 = 3, 4, 56, 98
# t3 = t1 + t2
#
# n1, n2, n3, *outros = t3
# print(n1, n2, n3, *outros)

# t1 = (1, 2, 'batata', 'a', 'Ismael')
# t2 = 5, 4, 89, 't', 'Yoko'  # Também é uma tupla (t2)
# t3 = 5,  # Também é uma tupla (t3)
# t4 = t2 + t1 + t3
# print(type(t1))
# print(type(t2))
# print(t1[4])
# print(t4)

# print(t1[1:])

# for v in t1:
#     print(v)
