#Valor pago no produto dependendo da condição de pagamento
preco = float(input('Digite o preço do produto: '))
print('''Valor será pago: 
1 - Dinheiro/Cheque 
2 - 1xCartão 
3 - 2xCartão 
4 - 3x ou mais no Cartão ''')
forma = int(input('Escolha a forma e digite: '))

if forma == 1:
    din = preco * 0.9
    print('O valor a ser pago com desconto de 10% no dinheiro é {} reais.'.format(din))
elif forma == 2:
    cartvis = preco * 0.95
    print('O valor a ser pago com desconto de 5% no cartão a vista é {} reais.'.format(cartvis))
elif forma == 3:
    cartparcd = preco / 2
    print('O valor a ser pago será duas vezes de {} reais.'.format(cartparcd))
elif forma == 4:
    print('Parcelamento a partir de 3 vezes tem juros de 20% acima do valor do produto.')
    qnt = int(input('Em quantas vezes? '))
    juros = preco * 1.2
    cartparctr = juros /qnt
    print('O valor a ser pago será {} vezes de {} reais. Valor total é {} reais'.format(qnt, cartparctr, juros))
else:
    print('Opção invalida!Tente novamente.')