from datetime import date
nasc=int(input("Ano de nascimento ? "))
atual= date.today().year
idade= atual- nasc
print("O atleta tem {} anos.".format(idade))
if idade <9:
    print('Classificação:MIRIM')
elif idade <= 14:
    print("Classificação:INFANTIL")
elif idade <= 19:
    print("classificação:JUNIOR")
elif idade <= 25:
    print("classificação:SENIOR")
else:
    print("classificação:MASTER") 

