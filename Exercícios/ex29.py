km = int(input('Qual a velocidade de seu carro? em km/h: '))
if km >= 80:
    print('Você ultrapassou a velocidade de 80 km/h e foi multado.')
    acd = km - 80
    mult = (acd * 7)
    print('O valor da multa é R$ {} reais.'.format(mult))
