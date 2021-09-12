#Emprestimo bancario
vlcasa = float(input('Digite o valor da casa R$ '))
sal = float(input('Digite o valor do seu sálario R$ '))
anos = int(input('Digite em quantos anos o empréstimo será feito: '))

prest = vlcasa / (anos * 12)
vlmax = sal * 0.3

if prest <= vlmax:
    print('Seu emprestimo foi aprovado o valor da prestação será de {:.2f} em {} anos'.format(prest, anos))

else:
    print('Seu emprestimo foi negado pois o valor da prestação ultrapassa 30% do seu sálario.')

