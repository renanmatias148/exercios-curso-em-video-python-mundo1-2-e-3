peso= float(input("Qual e seu peso?"))
altura=float(input("Qual e sua altura"))
imc=peso/(altura*altura)
print("O imc dessa pessoa é de {:.1f}".format(imc))
if imc <18.5:
    print("ABAIXO DO PESO")
elif imc <= 25:
    print("PESO IDEAL")
elif imc <= 30:
    print("SOBRE PESO")
elif imc <= 40 :
    print("OBESIDADE")
else:
    print("OBESIDADE MORBITA")