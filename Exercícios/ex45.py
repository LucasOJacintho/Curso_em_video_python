#Jokenpô
from random import choice
from time import sleep
print('Vamos jogar! pedra, papel ou tesoura?')
escolha = str(input('Digite: '))
print('Joo')
sleep(1)
print('kenn')
sleep(1)
print('pô!!')
sleep(1)
joq = ['pedra','papel', 'tesoura']
jogo = choice(joq)

if escolha == joq[0] and jogo == joq[2]:
    print('Pedra quebra tesoura, você ganhou!Parabéns.')
elif escolha == joq[0] and jogo == joq[1]:
    print('Papel embrulha a pedra, você perdeu!Tente numa proxima.')
elif escolha == joq[1] and jogo == joq[2]:
    print('Tesoura corta papel, você perdeu!Tente numa proxima')
elif escolha == joq[1] and jogo == joq[0]:
    print('Papel embrulha a pedra você ganhou! Parabéns.')
elif escolha == joq[2] and jogo == joq[1]:
    print('Tesoura corta papel, você ganhou. Parabéns ')
elif escolha == joq[2] and jogo == joq[0]:
    print('Pedra quebra tesoura, você perdeu!Tente numa proxima ')
elif escolha == joq[0] == jogo or escolha == joq[1] == jogo or escolha == joq[2] == jogo:
    print('Xii.. empatou ... ')

print("Sua esolha foi {}.".format(escolha))
print('A minha foi {}.'.format(jogo))
