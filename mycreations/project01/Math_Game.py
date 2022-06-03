from tracemalloc import stop
import random


def math():

    print('Dificuldade 1 tem numeros de 1 a 10 ')
    print('Dificuldade 2 tem numeros de 1 a 50 ')
    print('Dificuldade 3 tem numeros de 1 a 100 ')

    print()
    print('Escolha o nivel dificuldade')
    print('1 - 2 - 3')

    dificuldade = int(input('digite o nivel da dificuldade: '))

    if dificuldade == 1:
        n = random.randint(1, 10)
        n2 = random.randint(1, 10)

    elif dificuldade == 2:
        n = random.randint(1, 50)
        n2 = random.randint(1, 50)

    elif dificuldade == 3:
        n = random.randint(1, 100)
        n2 = random.randint(1, 100)

    #####
    print()
    print('O que quer aprender?')
    print('-----------------------------------------------')
    print('Use 1 para dividir')
    print('Use 2 para adicionar')
    print('Use 3 para multiplicar')
    print('Use 4 para subtrair')
    print()
    questao0 = int(input('Qual das atividades a cima: '))

                        # Divisão do código (Divisão)

    if questao0 == 1:
        n3 = n / n2
        start = (input('Pressione enter '))


        if start == '':
            print(f'{n} / {n2} =')
            ans = float((input('Sua Resposta: ')))
            print(f'A resposta era {n3:.2}')

        if ans == n3:
            print("Acertou!")
        else:
            print('Errou :(')

        print('Use "s" para concoradar e "n" para descordar')

        questao = input('Tentar novamente? (s ou n) ')

        if questao == 's':
            math()
        else:
            stop

                        # Divisão do código (SOMA)

    elif questao0 == 2:
        n3 = n + n2
        start = (input('Pressione enter '))

        if start == '':
            print(n, '+', n2, '=')
            ans = int((input('Sua Resposta: ')))
            print(f'A resposta era {n3}')

        if ans == n3:
            print("Acertou!")
        else:
            print('Errou :(')

        print('Use "s" para concoradar e "n" para descordar')

        questao = input('Tentar novamente? (s ou n) ')

        if questao == 's':
            math()
        else:
            stop

                        # Divisão do código (Multiplicação)

    elif questao0 == 3:
        n3 = n * n2
        start = (input('Pressione enter '))

        if start == '':
            print(n, '*', n2, '=')
            ans = int((input('Sua Resposta: ')))
            print(f'A resposta era {n3}')

        if ans == n3:
            print("Acertou!")
        else:
            print('Errou :(')

        print('Use "s" para concoradar e "n" para descordar')

        questao = input('Tentar novamente? (s ou n) ')

        if questao == 's':
            math()
        else:
            stop

            # Divisão do código (Subtração)

    elif questao0 == 4:
        n3 = n - n2
        start = (input('Pressione enter '))

        if start == '':
            print(n, '-', n2, '=')
            ans = int((input('Sua Resposta: ')))
            print(f'A resposta era {n3}')

        if ans == n3:
            print("Acertou!")
        else:
            print('Errou :(')

        print('Use "s" para concoradar e "n" para descordar')

        questao = input('Tentar novamente? (s ou n) ')

        if questao == 's':
            math()
        else:
            stop

math()
