n = int(input('Digite um numero: '))
for c in range(1, n+1):
    print(c)
print('fim!')

i = int(input('Digite o inico: '))
f = int(input('Digete o fim: '))
p = int(input('Digite o passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite a nota: '))
    s = s + n
print('O media da notas é {}'. format(s/4))

