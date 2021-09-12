#Como utilizar cores no terminal em python
#Usando o codigo ANSI '\033[m
#Style(0,1,4, 7)
#text(30 até 37)
#Background (40 até 47)
print('Olá mundo!')
print('\033[31mOlá mundo!')
print('\033[32;43mOlá mundo!')
print('\033[1;34;43mOlá mundo!')
print('\033[1;35;43mOlá mundo!\033[m')
print('\033[7;30;45mOlá mundo!\033[m')# 7 invente
print('\033[7;30mOlá mundo!\033[m')
n1 = 4
n2 = 5
print('a soma de \033[35m{}\033[m + \033[36m{}\033[m ??? '.format(n1, n2))

## uma forma é fazer no format
nome = 'Lucas'
print('Olá! Muito prazer {}{}{}!!'.format('\033[4;35m',nome, '\033[m'))

# outra forma é fazer um dicionario de para formatação
cores = {'limpa':'\033[m',
         'Azul':'\033[34m',
         'Amarelo':'\033[33m',
         'pretoecinza':'\033[7;30m'}
print('Olá! Muito prazer {}{}{}!!'.format(cores['Azul'],nome,cores['limpa']))
