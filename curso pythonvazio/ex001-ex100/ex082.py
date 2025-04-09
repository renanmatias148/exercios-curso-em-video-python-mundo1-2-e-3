#lista vazias
lista=[]
listapares=[]
listaimpares=[]
while True:# laco de reptiçao para que o programa rode ate break seja solicitado
    n=int(input('digite um valor:'))
    if n %2==0:
        listapares.append(n)#aqui para adicionar  os numeros pares na lista de pares
    else:
        listaimpares.append(n) #aqui para aducionar os numeros impares na lista de impares 
    lista.append(n) # aqui para adicionar os numeros digitados na lista completa
    r=str(input("que continuar? [s/n]"))
    if r in "Nn": # se caso a resposta da variavel r for "Nn" o laço de reptição 
        break # sera encerrado
print("-="*30)
print(f"A lista completa é {lista}")
print(f"A lista de pares é {listapares}")
print(f"A lista de impares é {listaimpares}")