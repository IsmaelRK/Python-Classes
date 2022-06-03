print('-----EXERCICIO 1')

digite = input('digite um número inteiro: ')

try:
    digite = int(digite)
    divisor = 2
    calculo = digite % divisor
    if calculo > 0:
        print('O número é impar')
    else:
        print('O número é par')
except:
    print('Digito inválido, tente novamente')

#######################
#######################

print('-----EXERCICIO 2')

pergunta_horas = input('Digite que horas são (use"." no lugar de ":"): ')


try:
    pergunta_horas = float(pergunta_horas)

    if pergunta_horas >= 0 and pergunta_horas <= 11.59:
        print('Bom Dia!')

    elif pergunta_horas >= 12 and pergunta_horas <= 17.59:
        print('Boa Tarde!')

    elif pergunta_horas >= 18 and pergunta_horas <= 23.59:
        print('Boa Noite!')
    elif pergunta_horas < 0 or pergunta_horas > 23.59:
        print('Inválido, digite um horário de 0-23!645')
except:
    print('Inválido, tente novamente.')

#######################
#######################

print('-----EXERCICIO 3')

nome = input('Digite seu nome: ')

qtd_nums = len(nome)

if qtd_nums <= 4:
    print('Seu nome é curto')
elif qtd_nums == 5 or qtd_nums == 6:
    print('Seu nome é normal')
elif qtd_nums >= 6:
    print('Seu nome é muito grande')









