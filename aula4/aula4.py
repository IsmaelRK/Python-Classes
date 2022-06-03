"""
Tipos de dados
str - string - textos 'Assim' "Assim"
int - inteiro - 123456 0 -10 -20  - 60 -1500 -1500
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93 0.0
bool - booleano/lógico - True/False 10 == 10
"""

print('Luiz', type('Luiz'))
print(10, type(10))
print(25.23, type(25.23))
print(10 == 10, type(10 == 10))  # quando == 2 sinais de igual estiverem juntos, esta sendo perguntado se isto é igual a isto
                         # '10 == 10' = '10 é igual 10?'
print(bool(""))

print('luiz', type('luiz'), bool('luiz'))  #converção str para bool

print('10', type('10'), type(int('10')))  #converção de str para int


# str, nome
print('Ismael', type('Ismael'))

# idade, int
print(14, type(14))

#altura, float
print(1.60, type(1.60))

# maior de idade?, bool
print(14 >= 18, type(14 >= 18))
