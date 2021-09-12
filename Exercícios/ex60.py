#primeria maneira de fazer fatorial
from math import factorial
print('Calcule seu fatorial')
print('**'*20)
num = int(input('Digite um numero: '))
fact = factorial(num)
print('O fatoral de {}! é {}.'.format(num, fact))

#Segunda maneira
print('\nCalcule seu fatorial')
print('**'*20)
num = int(input('Digite um numero: '))
c = num
mult = 1
while c > 0:
    mult = mult * c
    c -= 1
print('\nO fatorial de {}! é {}'.format(num,mult ))

#outra forma de fazer
print('Calcule seu fatorial')
print('**'*20)
num = int(input('Digite um numero: '))
c = num
mult = 1
print('O fatorial de {}! é:'.format(num))
while c > 0:
    print('{}'.format(c), end='')
    print('x' if c > 1 else '=', end='')
    mult = mult * c
    c -= 1
print(mult)

