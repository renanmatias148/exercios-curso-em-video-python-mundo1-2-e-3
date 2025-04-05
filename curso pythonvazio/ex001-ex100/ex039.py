from datetime import date
nascimento=int(input("Ano de NASCIMETO:"))
atual= date.today().year
idct= (atual- nascimento)
if idct == 18:
    print('Voçe tem que se alista IMEDIATAMEMTE!')
elif idct>= 18:
    print("Voçe devia ter se alistado a {} anos".format((idct-18)))
elif idct<= 18:
    print("Ainda falta {} anos para o alistamento".format((18-idct)))
    print("Seu alistamento deve ser em {}".format((18-idct+atual)))