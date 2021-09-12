print('Soma de ímpares mútiplus de três')
soma = 0
cont = 0
for c in range(1, 500):
    if c % 2 != 0:
        if c % 3 == 0:
            cont = cont + 1
            soma = soma + c

print('A soma dos {} números impares é {}.'.format(cont, soma))
