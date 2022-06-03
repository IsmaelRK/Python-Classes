"""
variavel = 'valor'  # Variavel global
variavel2 = 'segundo valor'  # Variavel global


def func():
    print(variavel)
    print(variavel2)


def func2():
    variavel = 'Outro Valor'
    print(variavel)  # Variavel local 'Global Modificada' só tem efeito localmente, neste caso apenas se altera em func2
    # Modificada no   ESCOPO LOCAL e não no ESCOPO GLOBAL.
    global variavel2  # A não ser que adicione a linha a esquerda, MAS NÃO É CONSIDERADA UMA BOA PRÁTICA.
    variavel2 = 'var'  # Pode causar comportamentos estranhos.
    print(variavel2)


func()
func2()

print(variavel)
print(variavel2)


def func3(arg=None):  # Uma maneira mais recomendada quando precisar trabalhar com variaveis de escopo global
    arg = arg.replace('v', 'c')
    return arg


another_var = func3(arg=variavel)
print(another_var)
"""

variavel = 'valor'


def func():  # Passando a variavel de um escopo global para local
    outra_var = 'valor'
    return outra_var


def func2(var):
    print(var)


var = func()
func2(var)
