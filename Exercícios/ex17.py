#Calculo da hipotesuna
from math import hypot
cat_op = float(input('Digite o comprimento do cateto oposto: '))
cat_adj = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(cat_op, cat_adj)
print('A sua hipotenusa é de {:.2f}'.format(hip))

#Forma mais simples de fazer sem importar bibliotecas
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hy = (co ** 2 + ca ** 2) ** (1/2)
print('A sua hipotenusa é de {:.2f}'.format(hy))
