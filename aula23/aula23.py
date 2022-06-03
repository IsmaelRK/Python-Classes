"""
listas em python
fatiamento
append, insert, pop, del, clear, extend +
min, max
range
"""
"""
#         0       1      2    3    4     5
lista = ["A", "Bacana", "C", "D", "E", 10.6]
#     -  6        5      4   3     2     1

lista[5] = 'Algo diferente'

string = "ABacanaCDE"


print(lista[1])
print(lista[-1])
print(string[1])
print(lista)
print(lista[0:3])
print(lista[2:])
print(lista[::2])   #Considere cada caráctere ao lado de ':' como: [inicio:fim:de quanto em quanto pular]
print(lista[::-1])  # '-' Inverte a lista

# Concatena

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2

print(l1)
print(l2)
print(l3)

# OU (com extend)

l1 = [1, 2, 3]
l2 = [4, 5, 6]

l1.extend(l2)

print(l1)
print(l2)

# ------------

l1.extend('AA')

print(l1)
# ------------

l2.append('AA2')

print(l2)
# ------------

l2.insert(0, 'batata')

print(l2)
print(l2[0])
"""
"""
l2 = [4, 5, 6]
l2.insert(0, 'batata')
print(l2)

l2.pop()
print(l2)

#################
#     0  1  2  3  4  5  6  7  8
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l2)
l2.insert(0, 'batata')
print(l2)

del(l2[0])
print(l2)

print(max(l2))
print(min(l2))
#################

l2 = list(range(0,10))
print(l2)

l2 = list(range(0,100,8))
print(l2)
#################

l2 = list(range(0,10))
print(l2)

soma = 0

for valor in l2:
    soma = soma + valor

print(soma)
"""
"""
l2 = ['string', True, 10, -20.9]

for elemento in l2:
    print(f'o elemento {elemento} e do tipo {type(elemento)}')
"""

palavra_secreta = 'caneta'
digitadas = []
chances = 3
while True:
    if chances < 1:
        print('Você Perdeu!')
        break


    letra_adivinha = input('Digite uma letra: ')

    if len(letra_adivinha) > 1:
        print('Isso não vale')
        continue

    digitadas.append(letra_adivinha)


    if letra_adivinha in palavra_secreta:
        print(f'Acertou! A letra {letra_adivinha} está correta!!')
    else:
        print(f'A letra {letra_adivinha} está incorreta')
        digitadas.pop()

    secreto_temp = ''
    for letra_sec in palavra_secreta:
        if letra_sec in digitadas:
            secreto_temp += letra_sec
        else:
            secreto_temp += '*'

    if secreto_temp == palavra_secreta:
        print(f'Parabéns, Você Ganhou!! A palavra era {secreto_temp}')
        break
    else:
        print(f'A palavra está da seguinte maneira: {secreto_temp}')

    if letra_adivinha not in palavra_secreta:
        chances -= 1
        print(f'Você possuiu {chances} chances')









































