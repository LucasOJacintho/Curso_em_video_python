#Primeiro e último nome da pessoa
nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
print('Primeiro = {}'.format(nome[0]))
print('Último = {}'.format(nome[-1]))
