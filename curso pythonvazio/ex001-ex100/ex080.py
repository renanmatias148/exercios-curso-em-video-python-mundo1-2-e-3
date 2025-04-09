lista=[]#criar uma lista vazia 
for c in range(0,5):#para 5 valores 
    n= int(input("digite  um valor"))#variavel para ler um valor
    if c ==0:#se e o primeiro valor 
        lista.append(n)#pode adicionar na lista 
    elif n > lista[len(lista)-1]:# se o numero for maior do numero que esta no ulmito elemento 
        lista.append(n)# pode adicinar na lista
    else:
        pos=0
        while pos < len(lista):#  enquanto a posiçao for menor que o tamanho da lista 
            if n <= lista[pos]:# vai verificar detro de cada posição se o numero que quer inserir se menor ou igual a ele   
                lista.insert(pos,n)# se ele for menor ou igual ele sera inserido numa posiçao especifica
                break #nao precisar que faça isso denovo vou da break pq sou vou inserir uma vez
            pos+=1#para ir passando para proxima posiçao
print(f"os valores digitados em ordem foram {lista}")#para mostra o resultado 
