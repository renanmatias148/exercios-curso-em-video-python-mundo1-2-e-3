listanum=[]
maior=menor=0
for c in range(0,5):
    listanum.append(int(input(f"digite um para posição {c}: ")))
    if c == 0:
        maior= menor =listanum[c]
    else:
        if listanum[c]> maior:
            maior=listanum[c]
        if listanum[c] < menor:
            menor=listanum[c]
print("-="*40)
print(f"Voce digitou os valores{listanum}")
print(f"o maior valor digitado foi {maior} nas posições ",end="")
for i, v in enumerate(listanum):
    if v == maior:
        print(f"{i}... ",end="")
print()
print(f"o menor valor digititado foi {menor} na posições ",end="")
for i,v in enumerate(listanum):
    if v == menor:
        print(f"{i}... ",end="")
print()
