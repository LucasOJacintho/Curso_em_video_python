valores = []
while True:
    valores.append(int(input('Digite um valor: ')))

    opcao = input('Quer continuar? [S/N]: ')
    if opcao in 'Nn':
        break
print(f'Foi digitado {len(valores)} valores na lista.')
valores.sort(reverse=True)
print(f'A lista ordenarna em ordem descrescente é {valores}')

if 5 in valores:
    print(f'O valor 5 está na lista na {valores.index(5)+1}º posição.')
else:
    print(f'O valor 5 não foi encontrado na lista')
