# Exercício 1
"""
def carta(saudacao, nome):
    print(saudacao, nome)



carta_in = input('Digite uma saudação: ')
carta_in2 = input('Digite um nome: ')
carta(carta_in, carta_in2)
"""

# Exercício 1
"""
def carta2(saudacao, nome):
    print(saudacao, nome)


carta2('Olá', 'Yoko')
"""

# Exercício 2
"""
def soma(n1, n2, n3):
    print(n1 + n2 + n3)


soma(1, 1, 1)
soma(1, 2, 2)
soma(5, 5, 5)
"""

# Exercício 3
"""
def percentual(val, perc):
    return valor + porcento


valor = 50
qts_porcento = 10
divisao = valor / 100
porcento = divisao * qts_porcento


print(percentual(valor, porcento))
"""


# Exercício 3 FORMA DO PROFESSOR!!!


# def aumento_percentual(valor, percentual):
#     return valor + (valor * percentual / 100)
#
# ap = aumento_percentual(50, 10)
# print(ap)
# ap = aumento_percentual(100, 10)
# print(ap)
# ap = aumento_percentual(10, 10)
# print(ap)
# ap = aumento_percentual(15, 100)
# print(ap)


# Exercício 4

# def fb(value):
#     if value % 5 == 0 and value % 3 == 0:
#         return f'FizzBuzz, {value} é divisível por 3 e 5'
#     if value % 3 == 0:
#         return f'fizz, {value} é divisível por 3'
#     if value % 5 == 0:
#         return f'buzz, {value} é divisível por 5'
#     return value
#
#
# from random import randint
#
# for n in range(100):
#     aleatorio = randint(0, 100)
#     print(fb(aleatorio))
