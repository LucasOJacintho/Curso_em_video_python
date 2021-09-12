print('##' * 10)
print('FAÇA A SUA TABUADA!')
print('##' * 10)
print('caso queira parar digite 0 ou numero negativo')
ont = mult = 0
while True:
    num = int(input('Digite a tabuada que quer: '))
    if num <= 0:
        break
    for cont in range(1, 11):
        mult = num * cont
        print(f'{num:2} x {cont:2} = {mult:2}')
print('Volte sempre!')
