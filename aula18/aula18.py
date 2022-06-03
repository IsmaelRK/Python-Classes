"""
Manipulando Strings
* String Indices
* Fatiamento de Strings [inicio:meio:fim]
* Funções built-in, len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html (tipos de built-in)
https://docs.python.org/3/library/functions.html (funções de built-in)
"""



# Positivos  [012345678]
texto =     'python s2'
# Negativos -[987654321]

print(texto [2])



url = 'www.google.com.br/'

print(url[:-1])

# Fatiando string
nova_string = texto[2:6]
print(nova_string)

nova_string = texto[:6]
print(nova_string)

nova_string = texto[7:]
print(nova_string)

nova_string = texto[-9]
print(nova_string)

nova_string = texto[-9:-3]
print(nova_string)

nova_string = texto[:-1]
print(nova_string)


nova_string = texto[0:6:2]  # Pulando caracteres, onde começa, onde termina e quantos pular
print(nova_string)

print(len(texto))



















