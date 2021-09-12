n1 = int(input('Digite o primeiro nuemro: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O  primeiro número {} é maior que o segundo {}.'.format(n1, n2))
elif n2 > n1:
    print('O segundo número {} é maior que o primeiro número {}'.format(n2, n1))
else:
    print('Não existe numero maior os dois são iguais')
