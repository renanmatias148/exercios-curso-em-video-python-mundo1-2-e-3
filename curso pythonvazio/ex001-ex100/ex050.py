soma=0
cad=0
for c in range (1,7):
    num=int(input("digite um valor "))
    if num % 2 ==0:
        soma= soma+ num 
        cad = cad + 1
print(f" Você informou {cad} valores PARES e a soma deles é {soma}")