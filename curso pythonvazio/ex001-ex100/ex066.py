cont=0
soma=0
while True:
    n=int(input("digite um valor:[999 para parar] "))
    if n == 999:
        break
    cont+=1
    soma+=n
print(f"a soma dos {cont} valores foi {soma}")