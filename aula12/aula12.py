"""
Operadores Lógicos - Aula 4
and, or, not
in e not in
"""

a = 2
b = 2
c = 3

print(a == b and  b > c)  # Com um argumento falso 'and' já o registra como falso

print(a > b or  b < c)  # Com um argumento verdadeiro 'or' já o registra como TRUE

a1 = 2
b1 = 3

if not b1 > a1:                 # Not inverte a expressão, True vira False e False vira True
    print('B é maior que A')

else:
    print('A é maior que B')



###########

"""
Como funciona o AND

VERDADEIRO E VERDADEIRO = TRUE
VERDADEIRO E FALSO = FALSE
FALSO E VERDADEIRO = FALSE
FALSO E FALSO = FALSE
comparacao1 AND comparacao2
"""

"""
Como funciona o OR

VERDADEIRO E VERDADEIRO = TRUE
VERDADEIRO E FALSO = TRUE
FALSO E VERDADEIRO = TRUE
FALSO E FALSO = FALSE
comparacao1 OR comparacao2
"""

a2 = 0

if not a2:                         # Neste caso se A2 estiver vazio print será executado, caso estiver com algo
    print('Preencha o valor de A2')  # dentro não executará.

# 0 também é considarado "false"


nome = 'Luiz OT'

if 'OT' in nome:             # o mesmo que perguntar: Existe a variavel 'OT' no seu nome? com o IN
    print('Existe no seu nome')

else:
    print('Não Existe')





if 'iz' not in nome:             # o mesmo que perguntar: Existe a variavel 'OT' no seu nome? com o IN e NOT
    print('Executei')

else:
    print('Existe')

print('----------------------------------------------------------------------------------------------')


usuario = input('Digite nome do Usuário: ')
senha = int(input('Digite sua Senha: '))

userbd = 'Ismael'
senhabd = 501

if usuario == userbd and senha == senhabd:
    print('Acesso Concedido')
else:
    print('Usuário e/ou senha inválidos')






