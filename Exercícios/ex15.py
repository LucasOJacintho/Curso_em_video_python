#Aluguel de carros
dias = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Qual foi a quantidade de kilometros percorridos? '))
tdias = dias * 60
tkm = km * 0.15
total = tdias + tkm
# total = (dias * 60) + (km * 0.15) mais simples 
print('O total a pagar pelo carro alugado é RS {:.2f} reais.'.format(total))
