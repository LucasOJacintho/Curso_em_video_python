#Aritmeticas

nome = input('Digite o seu nome:')

print('É um prazer te conhecer, {:^20}!'.format(nome))#alinhamento apartir do ^ centralizado
print('É um prazer te conhecer, {:>20}!'.format(nome))#alinhamento > a direita
print('É um prazer te conhecer, {:<20}!'.format(nome))#alinhamento <a esquerda
print('É um prazer te conhecer, {:*^20}!'.format(nome))# caracter (*) colocado entre : e ^ou <> será exibido

n1 = int(input('digite uma valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma é {}, o produto é {} e a divisão é {:.2f}'.format(s, m, d)) # formatar a quantidade de casas a serem exibidas de nuemros reais {:.2f}
print('A divisão inteira é {} e potencia {}'.format(di, e), end=', ') # concatenação de prints de usa o end
print('a soma é {},\n o produto é {} e a\n divisão é {:.2f}'.format(s, m, d)) # para quebrar linha \n