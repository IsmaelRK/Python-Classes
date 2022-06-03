import shutil
from zipfile import ZipFile

print(" ")
print(" ")
print('Atenção! Lembre-se de deixar os arquivos quais quer compactar ou descompactar na mesma pasta que o Programa!')

print('############')
print(' ')
print('Use 1 para usar o Compactador (.zip)')
print('Use 2 para usar o Descompactador (.zip)')
print(' ')
print('############')
print(' ')
print(' ')
pergunta = input('digite a opção correspondente: ')
pergunta = int(pergunta)

try:

    if pergunta == 1:

        arq_nome = input('Digite o nome da pasta: ')
        #new = input('Digite o nome da pasta novamente para renomear: ')


        shutil.make_archive(arq_nome,'zip', arq_nome)

    elif pergunta == 2:

        print('###')
        print('Escreva no formato EX: "arquivo.zip" (sem as aspás)')
        print('###')
        print(' ')

        arq_nome2 = input('Nome do Arquivo: ')

        ext = ZipFile(arq_nome2, 'r')
        ext.extractall()
        ext.close()

except:
    print('Ocorreu um Erro')
