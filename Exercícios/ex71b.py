print('¨*¨' * 10)
print('{:^30}'.format('BANCO NOEMI'))
print('¨*¨' * 10)

while True:
    valor = int(input('\nDigite o valor que quer sacar: '))
    ced = 50
    totalced = 0
    while True:
        if valor >= ced:
            valor -= ced
            totalced += 1
        else:
            if totalced > 0:
                print(f'Total {totalced} cédulas de R$ {ced},00 reais.')
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            totalced = 0
            if valor == 0:
                break
    opcao = input('Quer realizar um novo saque?[S/N]: ').strip().upper()[0]
    if opcao in 'N':
        break
print('Volte sempre!')
