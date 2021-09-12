frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
agrupo = ''.join(palavras)
inverte =''

# No for colocamos o conprimento da frase sem espaço -1 para a ultima letra tambe estar
# até -1 para a primera letra tambem estar com passo negativo para inverter.
for l in range(len(agrupo) -1, -1, -1):
    inverte += agrupo[l]
if inverte == agrupo:
    print('A frase {} invertida é {} e por isso é um políndromo'.format(agrupo, inverte))
else:
    print('A frase {} invertida é {}, mas não é um políndromo.'.format(agrupo, inverte))

# Outra forma de fase é por fatiamento

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
agrupo = ''.join(palavras)
inverte = agrupo[::-1]
if inverte == agrupo:
    print('A frase {} invertida é {} e por isso é um políndromo'.format(agrupo, inverte))
else:
    print('A frase {} invertida é {}, mas não é um políndromo.'.format(agrupo, inverte))