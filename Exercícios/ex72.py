numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito',
          'nove', 'dez', 'onze', 'doze', 'treze', 'cartorze', 'quinze', 'desseseis',
          'dezessete', 'desoito', 'dezenove', 'vinte')
while True:
    while True:
        valor = int(input('Digite um valor de 0 a 20: '))
        if 0 <= valor <= 20:
            break
        print('Tente novamente.', end='')
    print(f'O valor que você digitou é {numero[valor]}')
    opcao = input('Você quer continuar? [S/N]:').strip()[0]
    if opcao in 'Nn':
        break
