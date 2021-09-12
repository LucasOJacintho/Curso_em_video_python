from random import randint
cont = 0
print('=-=' * 8)
print('vamos jogar par ou impar')
print('=-=' * 8)
while True:
    valor = int(input('Escolha um valor: '))
    comp = randint(0, 11)
    soma = valor + comp
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('par ou impar? [P/I]')).upper().strip()[0]
    print(f'voce jogou {valor} e computador {comp}. Total é {soma} ', end='')
    print(f'deu par.' if soma % 2 == 0 else 'deu ímpar.')
    if escolha == 'P':
        if soma % 2 == 0:
            print('Você venceu, Parabéns!')
            cont += 1
        else:
            print('Xii, vocÊ perdeu.')
            break
    elif escolha == 'I':
        if soma % 2 != 0:
            print('Você venceu, Parabéns!')
            cont +=1
        else:
            print('Xii, vocÊ perdeu.')
            break
    print('Vaos jogar novamente? ')
print(f'GAME OVER! Você venceu {cont} vezes')