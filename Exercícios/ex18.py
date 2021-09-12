#Calculo de seno, cosseno e tangente
from math import sin, cos, tan, radians
ang = float(input('Digite o valor do ângulo: '))
ang_ra = radians(ang)
sen = sin(ang_ra)
cos = cos(ang_ra)
tan = tan(ang_ra)
print('O angulo {}, tem seu seno de {:.3f}, o cosseno de {:.3f} e a tangente de {:.3f}.'.format(ang, sen, cos, tan))

#Outrac forma de converte é usando uma funça~odentro da outra
#sen = sin(radians(ang))
