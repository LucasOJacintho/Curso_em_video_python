from datetime import date
nasc = int(input('Digite a data do seu nascimento: '))
ano = date.today().year
idade = ano - nasc
if idade == 18:
    print('É hora de se alistar!')
elif idade < 18:
    faltam = 18 - idade
    print('Você ainda vai se alistar ao serviço militar, falta {} anos.'.format(faltam))
    alist = ano + faltam
    print('Seu alistamneto será em {}.'.format(alist))
elif idade > 18:
    passou = idade - 18
    print('Você já passou do tempo do alistamento, já faz {} anos.'.format(passou))
    alist = ano - passou
    print('Seu alistamento foi em {}.'.format(alist))

