"""
Operador ternário em Python
"""
"""
logged_user = True

if logged_user:
    msg = 'logado'
else:
    msg = 'Usúario prescisa logar!'

print(msg)

print()
print()
print()
"""

"""
logged_user = False
msg = 'logado' if logged_user else 'Usuário prescisa logar!'

print(msg)
"""
idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Você deve digitar apenas números')
else:
    idade = int(idade)
    e_maior = (idade >= 18)
    msg = 'Acesso permitido' if e_maior else 'Acesso negado'

    print(msg)
