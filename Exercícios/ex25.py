#procurando uma string dentro de outra
nome = str(input('Digite o seu nome completo: ')).strip()
nome = nome.lower()
print('Seu nome contem Silva? {}'.format('silva' in nome))

