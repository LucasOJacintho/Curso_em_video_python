from random import choice
al1 = str(input('coloque o nome do aluno 1: '))
al2 = str(input('Coloque o nome do aluno 2: '))
al3 = str(input('Coloque o nome do aluno 3: '))
al4 = str(input('Coloque o nome do aluno 4: '))
lista = [al1, al2, al3,al4]
sort = choice(lista) #random.choice é para escolher um elemento aleatório
print('O aluno sorteado é {}'. format(sort))
