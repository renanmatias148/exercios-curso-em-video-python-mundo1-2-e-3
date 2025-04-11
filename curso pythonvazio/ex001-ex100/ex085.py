#lista vazias
lista=[]
listapares=[]
listaimpares=[]
for c in range(1,8):
    lista.append(int(input(f"digite {c}º um valor")))
for num in lista:
    if num%2 ==0:
        listapares.append(num)
    else:
        listaimpares.append(num)
listaimpares.sort()
listapares.sort()
print(f"Lista de numeros pares {listapares}")
print(f"lista de numros impares {listaimpares}")

  