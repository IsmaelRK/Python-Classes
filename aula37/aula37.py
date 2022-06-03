"""
Funções (def) em Python - *args **kwargs -
(Parte - 3)
"""


# def func(a1, a2, a3, a4, a5, nome=None, a6=None):
#     print(a1, a2, a3, a4, a5, nome, a6)
#     return nome, a6
#
#
# var = func(1, 2, 3, 4, 5, nome='Luiz', a6='5')
# print(var[0], var[1])

# def func(*args):
#     print(args)
#     print(args[0])
#     print(args[-1])
#     print(len(args))
#
#
# func(1, 2, 3, 4, 5)

# lista = [1,2,3,4,5]
# n1, n2, *n = lista
# print(n1, n2, n)
# print(lista)
# print(*lista, sep='-')  # sep, função á ser usada como separador, neste caso: -


# def func(*args):
#     args = list(args)
#     args[0] = 20
#     print(args)
#
#
# func(1, 2, 3, 4, 5)

# def func(*args):
#     for v in args:
#         print(v)
#
#
# lista = 1, 2, 3, 4, 5
# func(1, 2, 3, 4, 5)

def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['nome'])
    print(kwargs['sobrenome'])
    print(kwargs['nome'], kwargs['sobrenome'])
    nome = kwargs.get('nome')
    print(nome)
    idade = kwargs.get('idade')  # Ao usar "idade = kwargs.get('idade')" ao invés de "idade = kwargs ['idade']" evita erros
    if idade is not None:        # Caso idade(neste caso) não seja encontrada.
        print(idade)
    else:
        print('Não encontrado')


lista = [1, 2, 3, 4, 5]
lista2 = [100, 200, 300, 400, 500]
func(*lista, 10, 20, 30, 40, *lista2, nome='Luiz', sobrenome='Miranda', idade=30)
