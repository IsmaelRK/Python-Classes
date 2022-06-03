"""
Split, Join, Enumerate em Python
* Split -Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list

string = "O Brasil é o o o país do futebol, o Brasil é penta."
lista1 = string.split(' ')
lista2 = string.split(',')


for valor in lista1:
    print(f'A palavra {valor} apareceu {lista1.count(valor)}x na frase.')


palavra = ''
contagem = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que mais apareceu foi {palavra} ({contagem}x)')

string = "O Brasil é o o o país do futebol, o Brasil é penta."
lista1 = string.split(' ')
lista2 = string.split(',')

for valor in lista2:
    print(valor.strip().capitalize())


#  lista = ['O', 'Brasil', 'é', 'Penta']
# Pode se escrever uma lista assim. Ou de uma forma mais simples, do modo seguinte.

string = 'O Brasil é Penta'
lista = string.split(' ')
string2 = ','.join(lista)

print(string)
print(lista)
print(string2)
"""

"""
string = 'O Brasil é Penta'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])
"""

lista = [
    [0, 'Luiz'],
    [1, 'João'],
    [2, 'Maria'],
]
for indice, nome in lista:
    print(indice, nome)

print()
print()

lista2 = ['Luiz', 'João', 'Maria']

for indice2, nome2 in enumerate(lista2):
    print(indice2, nome2)

print('#################')

lista3 = ['Luiz', 'João', 'Maria']

n1, n2, n3 = lista3

print(n1)
print(n2)
print(n3)
