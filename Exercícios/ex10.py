#Conversor de moedas
qnt = float(input('Qual o valor que você tem na carteira? R$ '))
dolar = qnt / 5.04
euro = qnt / 6.14
print('Com R$ {} reais, você pode comprar US${:.2f} dólares ou pode comprar EUR$ {:.2f} euros.'.format(qnt, dolar, euro))
