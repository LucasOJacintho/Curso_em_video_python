#Pintando a parede, area da parede
larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
area = larg * alt
qntinta = area / 2
print('Sua parede tem {} X {} de dimensão e a área a ser pintada é de {} m².'.format(larg, alt, area))
print('A quantidade de tinta necessaria será de {} l, para pintar sua parede.'.format(qntinta))
