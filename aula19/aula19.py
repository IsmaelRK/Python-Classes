"""
while em python
utilizado para realizar ações enquanto uma condição for verdadeira

requisitos: Entender condiçoes e operadores
"""

"""
while True:
    nome = input("Qual o seu Nome: ")
    print(f'Olá {nome}')


print('Do lado de fora, não sera executada')
"""

"""
x = 0
while x < 10:
      if x == 3:
        x = x + 1
        break
      print(x)
      x = x + 1

print('Acabou!')

"""
"""
x = 0  # coluna



while x < 10:
    y = 0  # linha
    while y < 5:
        print(f'{x}, {y}')
        y += 1




    x += 1  # O mesmo que x = x +1





print('Acabou!!')

"""

while True:
    print()

    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    sair = input('Deseja Sair? [s] sim ou [n] não: ')

    if sair == 's':
        break

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você prescisa digitar um número.')
        continue

    num1 = int(num1)
    num2 = int(num2)

    # +, -, /, *

    if operador == '+':
        print(num1 + num2)

    elif operador == '-':
        print(num1 - num2)

    elif operador == '/':
        print(num1 / num2)

    elif operador == '*':
        print(num1 * num2)

    else:
        print('Operador invalido')



