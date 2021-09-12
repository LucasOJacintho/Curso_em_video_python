
print('Desenvolva sua progressão aritmética!')
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
ultitermo = int(input('Qual o ultimo termo: '))
prim = termo
c = 1
total = 0
print('*=*' * 15)
while ultitermo != 0:
    total = total + ultitermo
    while c <= total:
        print(' {} '.format(prim), end='')
        prim = prim + razao
        c += 1
    print('Pausa')
    ultitermo = int(input('Voce deseja adicionar masi termos? '))
print('***'*15)
print('Foram gerados {} termos de PA'.format(total))
