print("=="*10)
print("10 TERMOS DE UMA PA")
print("=="*10)
a1=int(input("Primeiro termo: "))
r=int(input("RAZAO"))
dec = a1+ (11-1) * r
for c in range (a1,dec,r):
    print(f"{c}",end=' -> ')
print("ACABOU")