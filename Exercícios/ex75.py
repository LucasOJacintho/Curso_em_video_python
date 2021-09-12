num = (int(input('Digite quatro numeros: ')),
       int(input('Digite quatro numeros: ')),
       int(input('Digite quatro numeros: ')),
       int(input('Digite quatro numeros: ')))

print(f'\nVocê digitou {num.count(9)} vezes o valor 9.')
if 3 in num:
    print(f'O valor 3 primeiro na {num.index(3) +1 }º posição.')
else:
    print(f'O valor 3 não foi digitado nenhuma vez.')

print(f'O números pares são: ', end='')
for n in num:
    if n % 2 == 0:
        print(f'"{n}" ', end='')
