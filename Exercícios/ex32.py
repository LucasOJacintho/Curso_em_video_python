from datetime import date # biblioteca para extrair do comutador a data atual
ano = int(input('Digite um ano qualquer: '))
if ano == 0:
    ano = date.today().year # importa apenas o ano
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto.'.format(ano))
else:
    print('O ano de {}, não é bissexto.'.format(ano))
