from random import choice, randint
from time import sleep
print('O computador está pensando em um numero aleatorio entre 0 e 5.')
num = int(input('Qual numero você acha que o computador pensou? De 0 a 5: '))
ale = [0,1,2,3,4,5]
sort = choice(ale)
if sort == num:
    print('Você venceu ele pensou em {}'.format(num))
else:
    print('Xii você perdeu o numero é {}'.format(sort))



#Outra forma de fazer o numero ALeatório usando as biliotecas randint e time sleep
comp = randint(0,5) #escolha aleatoria entre 0 e 5
print('-*-' * 20)
print('O computador está pensando em um numero aleatorio entre 0 e 5.')
print('-*-' * 20)
usi = int(input('em que numero ele pensou? '))
print('Processando...')
sleep(3)
if usi == comp:
    print('Você venceu ele pensou em {}'.format(usi))
else:
    print('Xii você perdeu o numero é {}'.format(comp))
