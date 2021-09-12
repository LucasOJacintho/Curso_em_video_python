# Devolução de numero inteiro por biblioteca ou de forma simples
from math import floor
num = float(input('Digite um numero: '))
inteiro = floor(num)
print('O número {} tem a parte inteira {}. '. format(num, inteiro))

#Outro metodo
import math
num = float(input('Digite um numero: '))
print('O número {} tem a parte inteira {}. '. format(num,math.trunc(num))) # trunc corta a parte real, deixando só a inteira

#Outra formar mais simples
num = float(input('Digite um numero: '))
print('O número {} tem a parte inteira {}. '. format(num,int(num)))