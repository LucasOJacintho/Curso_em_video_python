mulheres = pesIdade = homens = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo biologico [M/F]: ')).upper().split()[0]

    if idade >= 18:
        pesIdade += 1
    if sexo in 'Ff' and idade < 20:
        mulheres += 1
    if sexo in 'Mm':
        homens += 1
    opcao = str(input('Deseja continuar cadatrando? [S/N]: ')).upper().split()[0]
    if opcao in 'Nn':
        break

print('*-*' * 10)
print('Tipos de pessoas cadastradas')
print('*-*' * 10)
print(f'\nTotal de pessoas cadastradas com mais de 18 anos foram: {pesIdade}.')
print(f'Ao todo foram cadadrado(s): {homens} homens.')
print(f'E temos cadastrada(s): {mulheres} mulheres com mmenos 20 anos.')
