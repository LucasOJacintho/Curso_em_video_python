#Sequencia de fibonacci
termo = int(input('Quantos termos voce quer? '))
fn1 = 0
fn2 = 1
c = 3
print('='*30)
print('A sua sequencia fibonacci é: ')
print('{}  {} '.format(fn1, fn2), end='')
while c <= termo:
    fn = fn1 + fn2
    print(' {} '.format(fn), end='')
    fn1 = fn2
    fn2 = fn
    c += 1
print('')
print('='*30)

