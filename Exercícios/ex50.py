soma = 0
par = 0
for c in range(1, 7):#vai repetir 6 vezes a atividade
    num = int(input('Digite o primeiro número: '))
    if num % 2 == 0:
        soma = soma + num
        par += 1
print('A soma dos {} numeros digitados  pares é {}.'.format(par, soma))
