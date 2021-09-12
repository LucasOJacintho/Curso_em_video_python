from random import randint
from time import sleep

cont = 1
comp = randint(0, 10)
print('-*-' * 20)
print('O computador está pensando em um numero aleatorio entre 0 e 10.')
print('-*-' * 20)
usi = int(input('Em que numero ele pensou? '))
print('Processando...')
sleep(3)
if usi == comp:
    print('Parabéns você acentou de primeira o numero é {} mesmo.'.format(comp))
else:
    while usi != comp:
        if usi < comp:
            print('Xii você errou, é mais, tente novamente!')
            usi = int(input('em que numero ele pensou? '))
        elif usi > comp:
            print('Xii você errou, é menos, tente novamente!')
            usi = int(input('em que numero ele pensou? '))
        cont += 1
    if usi == comp:
        print('Você acertou ele pensou em {}, mas você tentou {} vezes.'.format(comp, cont))


