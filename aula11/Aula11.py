"""
Operadores Relacionais - Aula4
==, igualdade
>, maior que
>=, maior ou igual que
<, menor que
<= menor ou igual que
!= diferente que
"""
"""
print(2 == 2)  # == Checa a igualdade

N = 9  # int
N2 = 9  # str

V = 'Ismael'
V2 = 'R'

print(N, N2)
print(N == N2)

exp = V != V2

print(exp)

"""

nome = (input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

# Limites de idade minima e maxima:
idade_min = 20
idade_max = 30

print('-----------')

print(f'O nome digitado foi {nome} e a idade digitada foi {idade}.')

print('----')




if(idade >= idade_min and idade <= idade_max):
    print(f'{nome} PODE simular e/ou contratar um empréstimo.')

else:
    print(f'{nome} NÃO PODE simular e/ou contratar um empréstimo.')





