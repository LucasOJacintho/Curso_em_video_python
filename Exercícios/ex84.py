pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append((float(input('Digite o peso em kg: '))))
##teste para definir qual é o peso maior e menor
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opcao = input('Quer continuar cadastrando? [S/N]: ')
    if opcao in 'Nn':
        break
print('*' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas na lista.')
print(f'O maior peso da lista é {maior} kg que é o peso de ', end='')
for i in pessoas:
    if i[1] == maior:
        print(f'[{i[0]}] ', end='')

print(f'\nE o menor peso da lista é {menor} kg que é o peso de ', end='')
for i in pessoas:
    if i[1] == menor:
        print(f'[{i[0]}] ', end='')
