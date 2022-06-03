"""
Entrada de dados - Aula 3
"""

nome = input('Qual o seu nome? ')
idade = input('Quantos anos de vida você fez ou fará este ano? ')
ano = input('Em que ano você esta? ')
nascimento = int(ano) - int(idade)


"""
print(f'Usuário digitou {nome}'
      f' e o tipo da variavel é {type(nome)}')

print(f'Usuário digitou {idade}'
      f' e o tipo da variavel é {type(idade)}')
"""


print('-----------------')

print(f'O nome do usuário é {nome}, tem {idade} anos, esta no ano de {ano} e nasceu em {nascimento} ')


"""
N1 = int(input("Número para somar: "))  # Função int já integrada
N2 = input("Outro número para somar: ")

print(f'A soma a ser feira será {N1} + {N2}')

N2 = int(N2)  # Função int separada

print(f'O resultado é: {N1 + N2}')
"""