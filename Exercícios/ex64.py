soma = contador = 0
print('Digite os numeros para soma e 999 para interromper!')
num = int(input('Digite o numero: '))
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite o numero: '))
print('A soma dos {} numeros digitados é {}.'.format(contador, soma))
