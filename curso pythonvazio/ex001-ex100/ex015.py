km=int(input('quantos km voce percorreu?'))
dia=int(input('Por quantos dias voce alugou?'))
diaria= dia*60
kms= km*0.15
print('Voce tem a pagar R${}'.format((diaria+kms)))