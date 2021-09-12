print('Qual tabuada você quer saber? ')
tab = int(input('Digite o número da tabuada: '))
for c in range(1, 10+1, 1):
    mult = tab * c
    print('{} x {:2} = {:2}'.format(tab, c, mult))
