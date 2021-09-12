brasileirao = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino',
               'Flamengo', 'Athletico-PR', 'Atlético-GO', 'Ceará',
               'Internacional', 'Santos', 'Corinthians', 'Juventude',
               'Bahia', 'São Paulo', 'Fluminense', 'Cuiabá',
               'Sport', 'América-MG', 'Grêmio', 'Chapecoense')
print('==' * 60)
print(f'O classificação dos times {brasileirao}')
print('==' * 60)
print(f'Os cinco primeiro colocados são {brasileirao[0:5]}')
print('==' * 60)
print(f'Os quatro ultimos colocados são {brasileirao[16:]}')
print('==' * 60)
print('==' * 60)
print(f'Os times em ordem alfabética são {sorted(brasileirao)}')
print('==' * 60)
print('O time Chapecoense está na posição {}'. format(brasileirao.index('Chapecoense') + 1))
print('==' * 60)
print(f'O time Chapecoense está na {brasileirao.index("Chapecoense") +1}º posicao')