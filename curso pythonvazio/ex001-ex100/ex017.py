import math

opo=float(input('Comprimento do cateto oposto:'))
adj=float(input('Comprimento do cateto adjacente:'))
hip= math.hypot(opo,adj)
print('A hipotenusa vai medir {:.2f}'.format(hip))
