#Primeira e ultima ocorrencia de string
frase = str(input('Escreva uma frase: ')).strip().lower()
print('Na sua frase a letra A, aparece {} vezes'.format(frase.count('a')))
print('A letra A aparece primeiro na posião {}'.format(frase.find('a')+1))
print('A letra A aparece na ultima posião {}'.format(frase.rfind('a')+1))

