#Calculando descontos
preco = float(input('Qual o preço do produto? R$ '))
new = preco*0.95
print('O preço do produto é R$ {:.2f} reais, com 5% de desconto ele custa R$ {:.2f} reais'.format(preco, new))