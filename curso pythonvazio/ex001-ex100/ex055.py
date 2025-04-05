maior=0
menor=0
for n in range (1,6):
    peso =float(input(f"Peso da {n}° pessoa? "))
    if n == 1 :
        maior = n
        menor = n
    else: 
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f" menor peso {menor} ")
print(f" maior peso {maior} ")