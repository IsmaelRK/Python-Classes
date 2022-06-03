"""
Funções - def em Python (Parte 1)
"""


def saudacao(msg='Olá', nome='Usúario'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    # print(msg, nome)
    return f'{msg}, {nome}'


var = saudacao()
print(var)

"""
saudacao()
saudacao(nome='Zezinho', msg='Hi')
saudacao('Olá', 'Ismael')
saudacao('Oi', 'Luiz')
saudacao('Hello', 'Maria')
saudacao('Olá', 'João')
"""
