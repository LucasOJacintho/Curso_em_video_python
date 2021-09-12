valores = list()
for v in range(0, 5):
    valor = (int(input('Diigte um valor: ')))
    if v == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Valor adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                valores.insert(pos, valor)
                print(f'Valor inserido na posição {pos}')
                break
            pos += 1
print(f'A lista me ordem é {valores}')


