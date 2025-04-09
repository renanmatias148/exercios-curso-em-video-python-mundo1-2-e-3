numeros= list()
while True:
    n=int(input("digite um valor: "))
    if n not in numeros: #aqui qnd o numero que for digitado  na variavel N
        numeros.append(n)# e ele mao for um numero duplcado sera adicionado
        print("valor adicionado com sucesso")# e aparecera essa mensagem de sucesso
    else:# mas se caso for numero duplicado ele sera ignorado 
        print("valor duplicado! não vou adicionar...")# e aparecera essa de valor dublicado 
    r=str(input("quer continuar? [S/N]")).strip().upper() #string perguntando se quero continuar
    if r  in"Nn":# aqui qnd a respota for N a repetiçao sera para pelo 
        break #o break
print("-="*30)
numeros.sort()#isso para colocar os numeros em ordem 
print(f"voçe digitou os valores{numeros}")#isso para mostra a lista na tela
