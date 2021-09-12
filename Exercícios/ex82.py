valores = []
valores_pares = []
valores_impares = []
while True:
    valores.append(int(input('Digite um valor: ')))
    opcao = input('Quer continuar? [S/N]: ')
    if opcao in 'Nn':
        break

print(f'Lista completa {valores}.')

for i in range(0, len(valores)):
    if valores[i] % 2 == 0:
        valores_pares.append(valores[i])
    else:
        valores_impares.append(valores[i])
print(f'A lista de pares é {valores_pares}.')
print(f'A lista de impares é {valores_impares}.')
