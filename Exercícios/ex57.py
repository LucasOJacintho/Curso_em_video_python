print('='*5,
      'INFORME SEU SEXO BIOLÒGICO [M/F]',
      '='*5)
sexo = str(input('M/F: ')).strip().upper()[0] # para pegar somente a primeria leta [0] coloque o fatiamento

while sexo not in 'MF':
    print('Resposta Incorreta, digite novamente')
    sexo = str(input('M/F: ')).strip().upper()[0]
print('Seus dados foram armazenados.Obrigada!')

