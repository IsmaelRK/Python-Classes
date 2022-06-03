"""
# Funções que checam se um numero pode ser comvertido:
# isnumeric, isdigit, isdecimal.
# Checam apenas números positivos.

print(num1.isnumeric())
print(num2.isnumeric())

num1 = int(num1)
num2 = int(num2)

print(num1 + num2)
"""

# Função Try e Except, como se fosse tente executar, caso ocorra erro vá para Except e não mostre o erro.
# Evita a quebra do programa em caso de erro.

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')


try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
except:
    print('carácteres inválidos')






# Código do professor abaixo

"""
import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')


if is_number(num1) and is_number(num2):
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
else:
    print('carácteres inválidos')
"""






























