r1 = int(input('Digite o comprimento da primeira reta: '))
r2 = int(input('Digite o comprimento da segunda reta: '))
r3 = int(input('Digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('É um triangulo EQUILÁTERO, seus lados são iguais')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('É um triangulo ISÓCELES, dois lados são igual')
    elif r1 != r2 != r3 != r1:
        print('É um um triãngulo ESCALANO, todos os lados são diferentes.')
else:
    print('As retas não podem formar um triangulo.')





