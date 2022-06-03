# Podemos usar len para determinar caracteres ou para contalos.


usuario = input('digite seu usuario: ')

qtd_carcters = len(usuario)

print(usuario, qtd_carcters, type(qtd_carcters))

if qtd_carcters < 6:
    print('Erro, necessita-se 6 ou mais caracteres')
else:
    print('Você foi cadastrado com sucesso')


print('----------------------------------------------------------------------------')

string1 = input('digite alguma coisa: ')
string2 = input('digite alguma outra coisa: ')

print(f'A quantidade total de caracters digitados foram {len(string1) + len(string2)}.')

print('----------------------------------------------------------------------------')

print(len(string2))
print(string2.__len__())
