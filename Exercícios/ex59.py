from time import sleep
print('Programa de opções!!')
print('='*40)
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

esc = 0
while esc != 5:
    print('\nO que deseja fazer? ')
    print('='*40)
    print('''\n        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa''')
    print('=' * 40)
    esc = int(input('\nEscolha sua opção : '))
    if esc == 1:
        soma = n1 + n2
        print('\nA soma de {} + {} = {}.'.format(n1,n2,soma))
    elif esc == 2:
        mult = n1 * n2
        print('\nA multiplicação de {} x {} = {}.'.format(n1, n2, mult))
    elif esc == 3:
        if n1 < n2:
            print('O número maior entre {} e {} é {}'.format(n1, n2, n2))
        else:
            print('O numero maior entre {} e {} é {}.'.format(n1, n2, n1))
    elif esc == 4:
        n1 = float(input('Digite o primeiro novo número : '))
        n2 = float(input('Digite o segundo novo número: '))
    elif esc == 5:
        print('Obrigado por acessar.')
    else:
        print('Opção inválida, escolha entre 1 e 5')
    sleep(2)
