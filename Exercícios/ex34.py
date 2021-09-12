sal = float(input('Digite o valor do seu sálario: '))
if sal > 1250:
    newsal1 = sal * 1.1
    print('Seu salario de R$ {:.2f} teve o reajuste de 10 % e passa a ser R$ {:.2f}.'.format(sal, newsal1))
else:
    newsal2 = sal * 1.15
    print('Seu salario de R$ {:.2f} teve o reajsute de 15 % e passa a ser R$ {:.2f}.'.format(sal,newsal2))
