nome = 'ismael'  # str
idade = 14  # bool
altura = 1.60  # float
e_maior = idade > 18  # bool
peso = 55
imc = peso / (altura **2)


print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc}')  # perceba o f no inicio e as chaves '{}'

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')  # perceba o ':f' após 'imc', ele indica
                                                    # o número de casas decimais apos o '.', neste caso 2 casas.

print(f'{altura:.1f}')


print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome,idade,imc))
print('{0} tem {2} anos de idade e seu imc é {1}'.format(nome, idade, imc))  # a ordem no format é 0,1,2,3,4...
                                                                             # a qual pode ser modificada.

print('{n} tem {i} anos de idade e seu imc é {im}'.format(n= nome,i= idade,im= imc))
