r1= int(input("Primeiro segmento"))
r2= int(input("Segundo segmento"))
r3= int(input("Terceiro segmento"))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmimentos acima formam um TRIANGULO ", end='') 
    if r1 == r2 == r3:
        print( "Equilatero")
    elif r1 != r2 != r3 != r1:
        print( "Escaleno")
    else:
        print( "Isosceles")

else:
    print("Os segmentos acima não podem formam um TRIANGULO")