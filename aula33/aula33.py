# Gerador de CPF
from random import randint

cpf_num = str(randint(100000000, 999999999))
cpf_informado = cpf_num
tamanhocpf = len(cpf_num)

if cpf_num == cpf_num:

    cpfnum1 = ''
    cpfnum2 = ''
    cpfnum3 = ''
    cpfnum4 = ''
    cpfnum5 = ''
    cpfnum6 = ''
    cpfnum7 = ''
    cpfnum8 = ''
    cpfnum9 = ''
    cpfnum10 = ''

    for num in cpf_informado:
        cpfnum1 += cpf_informado[0]
        cpfnum2 += cpf_informado[1]
        cpfnum3 += cpf_informado[2]
        cpfnum4 += cpf_informado[3]
        cpfnum5 += cpf_informado[4]
        cpfnum6 += cpf_informado[5]
        cpfnum7 += cpf_informado[6]
        cpfnum8 += cpf_informado[7]
        cpfnum9 += cpf_informado[8]
        break

    cpfnum1, cpfnum2, cpfnum3 = int(cpfnum1), int(cpfnum2), int(cpfnum3)
    cpfnum4, cpfnum5, cpfnum6 = int(cpfnum4), int(cpfnum5), int(cpfnum6)
    cpfnum7, cpfnum8, cpfnum9 = int(cpfnum7), int(cpfnum8), int(cpfnum9)

    c1 = cpfnum1 * 10
    c2 = cpfnum2 * 9
    c3 = cpfnum3 * 8
    c4 = cpfnum4 * 7
    c5 = cpfnum5 * 6
    c6 = cpfnum6 * 5
    c7 = cpfnum7 * 4
    c8 = cpfnum8 * 3
    c9 = cpfnum9 * 2
    soma = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9
    calc = 11 - (soma % 11)

    if calc > 9:
        result_calc = 0
    else:
        result_calc = calc

    cb1 = cpfnum1 * 11
    cb2 = cpfnum2 * 10
    cb3 = cpfnum3 * 9
    cb4 = cpfnum4 * 8
    cb5 = cpfnum5 * 7
    cb6 = cpfnum6 * 6
    cb7 = cpfnum7 * 5
    cb8 = cpfnum8 * 4
    cb9 = cpfnum9 * 3
    cb10 = result_calc * 2
    somab = cb1 + cb2 + cb3 + cb4 + cb5 + cb6 + cb7 + cb8 + cb9 + cb10
    calcb = 11 - (somab % 11)

    if calcb > 9:
        result_calcb = 0
    else:
        result_calcb = calcb

    result_calcb = str(result_calcb)
    result_calc = str(result_calc)
    cpf_num += result_calc
    cpf_num += result_calcb
    print(cpf_num)
