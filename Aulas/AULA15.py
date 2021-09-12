num = sum = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    sum += num
#print('A soma dos numeros é {}'.format(sum))
print(f'A soma dos numeros é {sum:->10}')