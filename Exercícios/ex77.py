jantar = ('escondinho', 'arroz', 'feijao', 'alface', 'abobrinha')

for j in jantar:
    print(f'\nNa palavra "{j}" aparece as vogais: ', end='')
    for letras in j:
        if letras.lower() in 'aeiou':
            print(f'{letras} ', end='')
