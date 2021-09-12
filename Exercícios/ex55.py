pmenor = 0
pmaior = 0
for c in range(1, 6):
    peso = float(input('Digite o {}º peso: '.format(c)))
    if c == 1:
        pmenor = peso
        pmaior = peso
    else:
        if peso > pmaior:
            pmaior = peso
        if peso < pmenor:
            pmenor = peso

print('O menor peso é {}kg'.format(pmenor))
print('O maior peso é {}kg.'.format(pmaior))
