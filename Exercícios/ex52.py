total = 0
num = int(input('Digite um numero: '))
for c in range(1, num +1):
    if num % c == 0:# vai ser testado se é divisivel de 1 até a num digitado.
        total += 1 #soma a quantidade de vezes que foi dividido com resposta 0
if total == 2: # apenas quando dividido 2 vezes é considerado um numero primo
    print('É um número primo')
else:
    print('Não é um número primo!')
