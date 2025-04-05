dist= int(input("Qual e a distancia de sua viagem?"))
v1= dist* 0.50
v2= dist* 0.45
if dist > 200:
    print("voçe esta preste a fazer uma viagem de {}km e o preço da sua passagem sera de R${:.2f}".format(dist,v2))
else:
    print("voce esta preste a fazer uma viagem de {}km e o preço da sua passagem sera de R${:.2f}".format(dist,v1))