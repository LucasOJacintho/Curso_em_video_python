cont = soma = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um valor: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N]: ')).upper()
media = soma / cont
print('a media dos {} valores digitados é {}'.format(cont, media))
print('O maior numero é {} e o menor numero é {}.'.format(maior, menor))
