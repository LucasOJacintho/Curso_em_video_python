teste = list()
teste.append('Noemi')
teste.append(27)
galera = list()
galera.append(teste[:]) # copia da lista
teste[0] = 'Maria'
teste[1] = '19'
galera.append(teste[:])

#mostra a posição do elemento da lista dentro [0][0]
pessoas = [['Noemi', 27], ['Lucas', 29], ['Mellone', 3], ['Miriam', 1]]
print(pessoas[1][0])

#pegando os dados de um vez
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')

alunos = list()
dados = list()
for c in range(0, 3):
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite a idade: ')))
    alunos.append(dados[:])
    dados.clear() ## para limpar lista temporaria

totMaior = totMenor = 0
for p in alunos:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totMaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totMenor += 1
print(f'Temos {totMaior} maiores de idade e {totMenor} menores de idade.')

