soma = 0
idademaior = 0
nomemaisve = ''
qntmulheres = 0
for c in range(1, 4 +1 ):
    nome = str(input('Digite o nome da {}º pessoa: '.format(c))).strip()
    idade = int(input('Digite a idade da {}º pessoa: '.format(c)))
    sexo = str(input('Qual o sexo biológico da {}º pessoa [M/F]: '.format(c))).strip().upper()
    soma += idade

    if c == 1 and sexo in 'M':
        idademaior = idade
        nomemaisve = nome
    if sexo in 'M' and idade > idademaior:
        idademaior = idade
        nomemaisve = nome
    if sexo in 'F' and idade < 20:
        qntmulheres += 1

media = soma / 4
print('A média da idade das pessoas é {} anos'.format(media))
print('A idade do homem mais velho é {} e se chama {}.'.format(idademaior, nomemaisve))
print('No grupo existem {} mulher(es) com menos de 20 anos.'.format(qntmulheres))
