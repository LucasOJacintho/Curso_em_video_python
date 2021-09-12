dist = int(input('Qual é a distancia da sua viagem em km? '))
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print('O valor da sua passagem é R$ {:.2f} reais.'.format(preco))


# maneira simples a condicional na mesma linha
preco2 = dist * 0.5 if dist <= 200 else dist * 0.45
print('O valor da sua passagem é R$ {:.2f} reais.'.format(preco2))