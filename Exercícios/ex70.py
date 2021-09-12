print('*-*' * 10)
print('Saldao da Oferta')
print('*-*' * 10)
total = cont = preco = menor = prcont= 0
menorprod = ' '
while True:
    print('*-*' * 10)
    produto = str(input('Digite o produto: ')).strip()
    preco = float(input('Digite o preço: '))
    prcont += 1
    total += preco

    if preco > 1000:
        cont += 1

    if prcont == 1 or preco < menor:
        menor = preco
        menorprod = produto

    opcao = input('Quer continuar?[S/N]: ')
    if opcao in 'Nn':
        break
print('\nSaldão da Oferta')
print('*-*' * 10)
print(f'O total de gasto é R$ {total:.2f}')
print(f'{cont} produto(s) custa mais de 1000 reais')
print(f'O {menorprod} é produto de menor preço')
print('*-*' * 10)
