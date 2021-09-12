#Condição if e else
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 +n2)/2
print('Sua média final é {:.1f}.'.format(m))
if m >= 6:
    print('Você foi aprovado, parabéns!')
else:
    print('Você foi reprovado, estude para a recuperação.')

#Maneira simplificada
print('Parabens' if m >= 6 else'Reprovado')
