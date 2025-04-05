velocidade=int(input("qual e a sua velocidade atual ? "))
multa= (velocidade-80)*7
if velocidade>80:
    print("MULTADO!!!Voce excedeu o limite permitido de velocida que de 80km/h tera que paga uma multa de R${:.1F}".format(multa))
print("TENHA BOA VIAJEM, DIRIJA COM SEGURANÇA")