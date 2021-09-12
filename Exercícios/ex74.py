from random import randint
num = (randint(1, 100), randint(1, 100), randint(1, 100),
       randint(1, 100), randint(1, 100))
print(f'O numeros sorteados são: {num}', end='')
print(f'\nO menor nuemro é {min(num)}')
print(f'O maior numero é: {max(num)}')

#cont = 0
#while True:
    #num = randint(0, 100)
    #cont += 1
    #if cont > 5:
     #   break
    #lis = tuple(num)
    #print(f'{lis} ', end='')

