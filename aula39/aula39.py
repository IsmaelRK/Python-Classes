# Exercício 1

def funcao2():
    return "EXECUTADA"


def funcao1(func):
    return func()


executar = funcao1(funcao2)
print(executar)


# Exercício 2

def func2(name='Ismael'):
    return name


def func3(idade=14, cor_cabelo='escuro'):
    return idade, cor_cabelo


def mestra(arg, arg2):
    return arg(), arg2()


executar2 = mestra(func2, func3)
print(executar2)
