#Cadeias de caracteres strings
frase = str('  Curso  em Video Python  ')
print(len(frase)) #tamanho da frase
print(frase.count('o')) # quantas vezes aparece a letra
print(frase.count('o',0, 13)) #Quantas vezes aparece a letra dentro do range (sempre o ultimo não é considerado
print(frase.find('deo')) #quantas vezes ele encontrou a stg a ua posição
print(frase.find('android')) #irá retornar -1 dizendo que a palavra não existe
print('Curso' in frase)

#Transformação
print(frase.replace('Python','Android')) #substitui a primeira str a segunda str
print(frase.upper())#trasforma todas a letras em mauisculas
print(frase.lower())#transforma todas as letras em minusculas
print(frase.capitalize())#joga a primeira letra da frase em maiuscula
print(frase.title())#transforma em maiuscula todas a primeiras letras de cada palavra
print(frase.strip())#remove espaço a mais das extremidades
print(frase.rstrip())#remove somente os espaço da direita da frase (right)
print(frase.lstrip())#remove espaço somente da esquerda da frase (left)

#divisão
print(frase.split())# gera uma lista divide a frase em lista pelas palavras
frase = frase.split() # para atribuir o valor em uma variavel e assim alterar
print(frase[1]) #mostra a palavra ou str da lista
print(frase[0][1:3])#mostra a letra da palavra da lista
print(' '.join(frase))# juntas as palavras da lista novamente. ('-') entre as aspas é o que irá ficar entre as palavras



