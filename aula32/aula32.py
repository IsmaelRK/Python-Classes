explicacao = 'O CPF deve conter os números, pontos(.) e traços(-), que no total resultarão em 14 caracteres'
print(f'{explicacao}.')
cpf_informado = input('Digite um CPF: ')
tamanhocpf = len(cpf_informado)
try:
    if tamanhocpf == 14:

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
        cpfnum11 = ''

        for num in cpf_informado:
            cpfnum1 += cpf_informado[0]
            cpfnum2 += cpf_informado[1]
            cpfnum3 += cpf_informado[2]
            cpfnum4 += cpf_informado[4]
            cpfnum5 += cpf_informado[5]
            cpfnum6 += cpf_informado[6]
            cpfnum7 += cpf_informado[8]
            cpfnum8 += cpf_informado[9]
            cpfnum9 += cpf_informado[10]
            cpfnum10 += cpf_informado[12]
            cpfnum11 += cpf_informado[13]
            break

        cpfnum1, cpfnum2, cpfnum3 = int(cpfnum1), int(cpfnum2), int(cpfnum3)
        cpfnum4, cpfnum5, cpfnum6 = int(cpfnum4), int(cpfnum5), int(cpfnum6)
        cpfnum7, cpfnum8, cpfnum9 = int(cpfnum7), int(cpfnum8), int(cpfnum9)
        cpfnum10, cpfnum11 = int(cpfnum10), int(cpfnum11)

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

        if cpfnum10 == result_calc and cpfnum11 == result_calcb:
            print('Este CPF é Valido!')
        else:
            print('Este CPF é Invalido!')

    else:
        print('Erro, o CPF não possui 14 caracteres.')

except:
    print('ERRO, verifique se você esta digitando o CPF da forma qual foi explicada acima.')
