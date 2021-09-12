from datetime import date
contmaior = 0
contmenor = 0
for c in range(1, 7 +1):
    ano = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    atual = date.today().year
    idade = atual - ano
    if idade > 18:
        contmaior += 1
    else:
        contmenor += 1
print('Temos {} pessoas maiores de idade'.format(contmaior))
print('Temos {} pessoas menor de idade'.format(contmenor))
