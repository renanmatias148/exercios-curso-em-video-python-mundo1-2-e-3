import math
ang=float(input('Digite o angulo que deseja?'))
seno= math.sin(math.radians(ang))
cosseno= math.cos(math.radians(ang))
ngente= math.tan(math.radians(ang))
print("O angulo de {} tem seno de {:.2f}".format(ang,seno))
print('O angulo de {} tem cosseno de {:.2f}'.format(ang,cosseno))
print('O angulo de {} tem tangente de {:.2f}'.format(ang,ngente))