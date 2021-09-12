from random import shuffle

al1 = str(input('coloque o nome do aluno 1: '))
al2 = str(input('Coloque o nome do aluno 2: '))
al3 = str(input('Coloque o nome do aluno 3: '))
al4 = str(input('Coloque o nome do aluno 4: '))
lista = [al1, al2, al3, al4]
shuffle(lista)
# para aparecer a ordem da lista a funcação não pode ser..
# ..atribuida a uma nova variavel
print('A sequencia dos alunos são: {}'.format(lista))


