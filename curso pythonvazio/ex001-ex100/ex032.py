ano= int(input('qual ano que analise ?Coloque 0 analisamos anoa atual: '))
if ano % 4 == 0 and ano % 100 != 0  or ano % 400 == 0:
    print('o ano {} e BISSEXTO'.format(ano))
else:
    print(' O ANO {} foi ano BISSEXTO'.format(ano))