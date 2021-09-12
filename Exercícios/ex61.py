print('Desenvolva sua progressão aritmética!')
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
#ultitermo = int(input('Qual o ultimo termo: '))
prim = termo
c = 1
print('O dez primeiros termos são : ')
print('*=*' * 15)
while c <= 10:
    print(' {} '.format(prim), end='')
    prim = prim + razao
    c += 1
print('*=*' * 15)