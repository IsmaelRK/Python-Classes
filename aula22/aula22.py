"""
For in em python
Iterando strings com for
Função range(start=0, stop, step=1)

"""

# continue pula para o próximo laço
# break para a execução do laço


texto = 'Python'

for letra in texto:
    print(letra)

print()

for n in range(20, 10, -1):
    print(n)

print()

for n in range(100):
    if n % 8 == 0:
        print(n)

print()

palavra = 'python'
nova_str = ''


for letr in palavra:
    if letr == 'y':
        nova_str = nova_str + letr.upper()
    elif letr == 'o':
        nova_str = nova_str + letr.upper()
    else:
        nova_str += letr

print(nova_str)
