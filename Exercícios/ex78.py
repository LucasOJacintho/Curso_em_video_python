numero = list()
for num in range(0, 5):
    numero.append(int(input('Digite um numero: ')))

print('-=-'*20)
print(f'O maior numero digitado foi o {max(numero)} e ele está na posição: ', end='')
for i, v in enumerate(numero):
    if v == max(numero):
        print(f'{i + 1}...', end='')

print(f'\nO menor numero digitado foi o {min(numero)} e ele está ma posição: ', end='')
for i, v in enumerate(numero):
    if v == min(numero):
        print(f'{i + 1}...', end='')
