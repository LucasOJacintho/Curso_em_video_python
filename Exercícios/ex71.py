print('¨*¨' * 10)
print(f'   BANCO NOEMI    ')
print('¨*¨' * 10)

while True:
    valor = int(input('\nDigite o valor que quer sacar: '))
    notas50 = valor // 50
    rest = valor - notas50 * 50
    notas20 = rest // 20
    rest2 = rest - notas20 * 20
    notas10 = rest2 // 10
    rest3 = rest2 - notas10 * 10
    notas1 = rest3 // 1

    print(f'Total {notas50} cédulas de R$ 50,00 reais')
    print(f'Total {notas20} cédulas de R$ 20,00 reais')
    print(f'Total {notas10} cédulas de R$ 10,00 reais')
    print(f'Total {notas1} cédulas de R$ 1,00 real')
    print('¨*¨' * 10)
    opcao = input('\nDeseja fazer um novo saque? [S/N]: ')
    if opcao in 'Nn':
        break
print('Volte sempre!')
