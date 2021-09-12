#Verificando as primeiras letras de um texto
cid = str(input('Digite o nome da sua cidade: ')).strip()
print('O nome da sua cidade começa com Santo? {}'.format(cid[:5].lower() == 'santo'))
