#Conversor de medidas: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n1 = float(input('Digite o valor em metros: '))
cent = n1 * 100
mili = n1 * 1000
print('O valor em centimetros é {:.0f} cm e o valor em milimentros é {:.0f} mm'. format(cent, mili))
