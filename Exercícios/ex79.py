valores = list()

c = 0
while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in valores:
        valores.append(valor)
        print('O valor foi adicionado com suceso')
    else:
        print(f'O valor já exite!Não vou adicionar')

    opcao = input('Quer adicionar mais valores?[S/N]: ')
    if opcao in 'Nn':
        break

valores.sort()
print('*' * 40)
print(f'Os valores digitados foram {valores}')
