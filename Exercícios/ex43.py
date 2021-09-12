peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
pemin = 18.5 * (altura ** 2)
pemax = 24.9 * (altura ** 2)
if imc < 18.5:
    print('Você está abaixo do peso, seu IMC é {:.1f}.'.format(imc))
    print('Seu peso ideal o minimo é {:.1f} e o maximo {:.1f}.'.format(pemin, pemax))
elif 18.5 <= imc < 25:
    print('Você está com o peso ideal, seu IMC é {:.1f}.'.format(imc))
elif 25 <= imc < 30:
    print('Você está com sobrepeso, seu IMC é {:.1f}.'.format(imc))
    print('Seu peso ideal o minimo é {:.1f} e o maximo {:.1f}.'.format(pemin, pemax))
elif 30 <= imc < 40:
    print('Você está com obesidade, seu IMC é {:.1f}.'.format(imc))
    print('Seu peso ideal o minimo é {:.1f} e o maximo {:.1f}.'.format(pemin, pemax))
elif imc >= 40:
    print('Você está com obesidade morbida, seu IMC é {:.1f}.'.format(imc))
    print('Seu peso ideal o minimo é {:.1f} e o maximo {:.1f}.'.format(pemin, pemax))
