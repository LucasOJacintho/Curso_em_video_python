print('=*='*19)
print('Digite os numeros para somar caso queira parar digite 999')
print('=*='*19)
som = cont = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    som += num
    cont += 1
print(f'Voce digitou {cont} e a soma é {som}.')
