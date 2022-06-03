nome = 'Luiz'
idade  = 32
altura = 1.80
peso = 80
ano = 2019
idade_da_pesoa = ano - idade
imc= peso / (altura **2)

print(f'{nome} tem {idade} anos, {altura:1} de altura e pesa {peso}kg.')
print(f'O imc de {nome} é {imc:.2f}.')
print(f'Luiz nasceu em {idade_da_pesoa}.')
