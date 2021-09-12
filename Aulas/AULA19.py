#DICIONARIOS

pessoas = {'nome': 'Noemi', 'sexo': 'F', 'idade': 27}
##Quabod está dentro de aspas simples é nescessario usar aspas duplas
##para puxar o elemento deve estar entre [..] do dicionario

print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys()) ## mostra as chaves nome, sexo, idade
print(pessoas.values()) ## mostra o valor dos elementos
print(pessoas.items())##mostra tudo

for c in pessoas.keys():# apenas as chaves em linhas
    print(c)
for c in pessoas.values(): # apenas os valores do elementos
    print(c)
for c, v in pessoas.items(): # mostra os itens com seus elementos por linha
    print(f'{c} = {v}') ##nõa precisa do enumerate

del pessoas['sexo'] ### ele apaga o elemento inteiro
pessoas['nome'] = 'Lucas' ## troca, modifica o elemento de dentro da chave
pessoas['peso'] = 96 ## adiciona uma nova chave com um novo elemento

brasil = []
estado1 = {'UF': 'São Paulo', 'sigla': 'SP'}
estado2 = {'UF': 'Santa Catarina', 'sigla': 'SC'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['UF']) ###MOSTRA O ELEMENTO sem chave

pais = list()
estados = dict()

##primeiro for capta os dados e copia para a lista
for c in range(0,3):
    estados['estado'] = str(input('Digite o nome do estado: '))
    estados['UF'] = str(input('digite a sigla do estado: '))
    pais.append(estados.copy()) ## para copiar os dados para a lista

## segundo for motra cada estado, cada dicionario
for e in pais:

##terceiro for mostra apenas os elementos das chaves
    for v in e.values():
        print(v, end=' ')
    print()