

n1 = int(input('Digite um numero: '))
print('''Você deseja convertar para:
1 - Binário 
2 - octal
3 - hexadecimal''')
base = int(input('Digite o número correspondente a conversão: '))
if base == 1:
    binario = bin(n1)[2:]
    print('O numero {} em binário é {}'.format(n1, binario))
elif base == 2:
    octal = oct(n1)[2:]
    print('O numero {} em octal é {}.'.format(n1, octal))
elif base == 3:
    hexadc = hex(n1)[2:]
    print('O numero {} em hexadecimal é {}.'.format(n1, hexadc))
else:
    print('Opção invalida.')

