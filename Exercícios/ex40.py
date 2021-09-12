nt1 = float(input('Digite a primeira nota: '))
nt2 = float(input('Digite a segunda nota: '))
media = (nt1 + nt2) / 2
if media < 5:
    print('VocÊ foi reprovado sua média é {:.1f}.'.format(media))
elif 5 <= media <= 6.9:
    print('Você está em recuperação, sue média é {:.1f}.'.format(media))
elif media > 7:
    print('Você foi aprovado, sua média é {:.1f}.'.format(media))