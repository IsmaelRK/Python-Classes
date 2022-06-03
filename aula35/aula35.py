"""
Funções - def em Python (Parte 2)
"""

# return retorna o valor da variavel (No script abaixo var recebe o valor abaixo e return "Transmite" este valor )
"""
def funcao(var):
    print('Isso não sera executado')
    return var


variavel = funcao('valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum Valor')
"""

"""
def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2


divide = divisao(8, 4)
if divide:
    print(divide)
else:
    print('Conta Inválida')
"""

"""
def dumb():
    return True


var = dumb()
print(var, type(var))
"""

"""
def f(var):
    print(var)


def dumb():
    return f


var = dumb()
print(id(var), id(f)) 

if var == f:
    print('var é igual a f')
else:
    print('não é igual')
"""


def dumb():
    return ('Luiz', 'Otávio')  # Tuple: Neste caso Luiz é o indice 1 ([0]) e Otávio ([1]) também


var = dumb()

print(var[1], type(var))
