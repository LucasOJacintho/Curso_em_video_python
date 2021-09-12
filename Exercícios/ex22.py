#Analisador de textos
nome = str(input('Escreva seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
nome = (nome.split())
Nc = (''.join(nome))
print('O seu nome completo tem {} letras.'.format(len(Nc)))
#print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' '))) subtraindo os espaços contidos no nome
print('E o seu primeiro nome tem {} letras.'.format(len(nome[0])))
