#AULA DE WHILE

# meu contador começa com 1.
c = 1
#no While: enquanto o valor for menor do que 10 ele vai repetir o laço e soma 1 até chegar
# no 10 e parar.Se for logica de maior ou menor ele para no antescessor se for = ele para
#exatamente no limite.
while c < 10:
    print(c)
    c += 1
print('FIM')

#while com condição de parada (flag) ele para quando digitado 0
#com inicio do contador em 1.
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')

#Outro exemplo
resp = 'S'
while resp == 'S':
    m = int(input('Digite um valor: '))
    resp = str(input('Quer continuar [S/N]: ')).upper()
print('FIM')

#Exemplo de programa dizendo quantos numeros são pares e quantos são impares

num = 1
par = impar = 0
while num != 0:
    num = int(input('Digite um valor: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print('Foi digitado {} pares e {} impares.'.format(par, impar))
