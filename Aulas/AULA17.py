lista = [2,5,7,6,9,3,1]
lista[2] = 3
lista.append(7) # ADICIONA itenm no final da lista
lista.sort() # Organiza a lista em ordem crescente
lista.sort(reverse=True) #Organiza a lista em ordem descrecente
lista.insert(3, 4) # adiciona item na lista (posição, elemento)
if 10 in lista:
    lista.remove(7) #remove o primeiro elemento encontrado
else:
    print('Não achei o item na lista')
print(lista)
print((f'Essa lista tem {len(lista)} itens'))

#Adicionando valores na lista pelo append
valores = list()
valores.append(5)
valores.append(9)
valores.append(3)
valores.append(1)

for valor in valores:
    print(f'{valor}...',end='')
print(f'\n')

for indice, valor in enumerate(valores):
    print(f'Na posição {indice} encontrei o valor {valor}!')

#lendo numeros pelo telclado
numeros = list()
for num in range(0, 4):
    numeros.append(int(input('Digite um numero:')))

listA = [2, 6, 8, 7]
listB = listA # dessa forma ela só espelha a lista
listB = listA [:] # assim ela faz a cópia em B