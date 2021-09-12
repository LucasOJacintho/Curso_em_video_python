papelaria = ('Lapis', 2.00, 'Caderno', 30.00,
             'Caneta', 3.50, 'Folha sulfite', 20.90,
             'Estojo', 15.80, 'Mochilas', 99.90)

print('---' * 12)
print(f'{"PAPELARIA MI":^30}')
print('---' * 12)

for p in range(0, len(papelaria)):
    if p % 2 == 0:
        print(f'{papelaria[p]:.<20}', end='')
    else:
        print(f'{papelaria[p]:.>10.2f}')
print('---' * 12)
