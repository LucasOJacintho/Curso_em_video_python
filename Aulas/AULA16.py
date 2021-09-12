#TUPLAS é imutavel

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
cafe = ('Café', 'Chá', 'Toddy')
alimento = lanche + cafe

print(alimento) #mostra as tupla juntas sequneciais
print(len(alimento))#tamanho da tupla
print(alimento.count('Suco'))#mostra quantas vezes se repete o item pedido
print(alimento.index('Pizza')) # em que posição está o elemento
print(sorted(lanche)) #coloca a tupla em ordem para mostrar

#for quando não precisa de posição
for comida in lanche:
    print(f'Eu vou comer {comida} de lanche')
#for quando precisa de posiçao
for cont in range (0, len(lanche)):
    print(f'Eu vou pegar {lanche[cont]} na posição {cont}')
#for quando precisa de posição
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi bastante')

# Nas tuplas podem ter dados diferentes
pessoa = ('Noemi', 1.65, 95, 'branca')
print(pessoa)
