#       Índices
#        0123456789......................33
#       Itereação atp de percorrer cada um dos elementos de uma string

frase = 'o rato roeu a roupa do rei de roma'
tam_frase = len(frase)

contador = 0
nova_string = ''
letra_do_user = input('Digite a letra: ')

while contador < tam_frase:
    letra = frase[contador]

    if letra == letra_do_user:
        nova_string += letra_do_user.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)
