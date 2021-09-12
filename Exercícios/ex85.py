numeros = list()
nume_pares = list()
nume_impares = list()
for cont in range(0, 7):
    numeros.append(int(input(f'Digite o {cont + 1}º numero: ')))

print(numeros)
for i in range(0, len(numeros)):
    if numeros[i] % 2 == 0:
        nume_pares.append(numeros[i])
    else:
        nume_impares.append(numeros[i])
nume_pares.sort()
nume_impares.sort()
print(f'A lista de numeros pares é {nume_pares}')
print(f'A lista de numeros impares é {nume_impares}')
