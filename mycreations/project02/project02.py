# Jokenpó

import random

random_num = random.randint(1, 3)

print('Digite: ')
print('1 para "pedra"  ')
print('2 para "papel"  ')
print('3 para "tesoura"')
question = input('Digite o número correspondente: ')



try:
    question = int(question)



    if random_num == 1:
        print('O escolhido pelo adversário foi pedra')

    elif random_num == 2:
        print('O escolhido pelo adversário foi papel')

    elif random_num == 3:
        print('O escolhido pelo adversário foi tesoura')
except:
    print('Erro, por favor, digite algum dos caracteres correspondentes (1, 2 ou 3), como informado a cima')


e = 'Empate!'
v = 'Você Ganhou!'
p = 'Você Perdeu!'


if question == 1 and random_num == 1:
    print(e)
elif question == 2 and random_num == 2:
    print(e)
elif question == 3 and random_num == 3:
    print(e)
elif question == 1 and random_num == 2:
    print(p)
elif question == 2 and random_num == 3:
    print(p)
elif question == 3 and random_num == 1:
    print(p)
elif question == 1 and random_num == 3:
    print(v)
elif question == 2 and random_num == 1:
    print(v)
elif question == 3 and random_num == 2:
    print(v)

