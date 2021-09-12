#Confederação de Natação por categoria de idade
from datetime import date
nasc = int(input('Digite o ano do seu nascimento: '))
ano = date.today().year
idade = ano - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Você está na categoria MIRIM.')
elif 9 < idade <=14:
    print('Você está na categoria INFANTIL.')
elif 14 < idade <= 19:
    print('VocÊ está na categoria JUNIOR.')
elif 19 < idade <= 20:
    print('Você está na categoria SENIOR.')
elif idade > 20:
    print('Você está na categoria MASTER.')
