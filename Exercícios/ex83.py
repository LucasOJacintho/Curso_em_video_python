lista = []
expressao = str(input('Digite uma expressão: '))
expressao_lis = [expressao]

print(expressao_lis)
for i in range(0, len(expressao_lis)):
    lista += expressao_lis[i]

aberto = lista.count('(')
fechado = lista.count(')')

if aberto == fechado:
    print('Sua espressão é valida')
else:
    print('Sua expressão é invalida, falta parenteses')

print('=='*15)
### está correta
expre = str(input('Digite me expressão matematica'))
pilha = []
for simb in expre:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
             pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua espressão é valida')
else:
    print('Sua expressão é invalida, falta parenteses')
