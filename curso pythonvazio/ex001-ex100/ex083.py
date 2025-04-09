exp=str(input("digite a expressão: "))
pilha=[]
for simb in exp:#para verificar cada simbolo cada empressao
    if simb=="(":# se simbolo for igual parenteses abrindo
        pilha.append("(") # vai  adicionar um elemento a pilha
    elif simb == ")":# se o simbolo for igual paranteses fechando
        if len(pilha) > 0:# vai vericifcar se tamanho da pilha e maior que 0 e sinal que nao esta vazio 
            pilha.pop() #entao vai remover o ultimo elemento
        else:# vai verificar se pilha estiver vazia
            pilha.append(")") #vai adiconar um elemento a pilha
            break #vai para  o laço 
if len(pilha) == 0:#aqui vai verificar se a pilha esta vazia 
    print("Sua expressão está valida!")#se estiver vai aparecer essa mensagem na tela 
else:# se caso nao estiver 
    print("Sua expressão está errada!")#vai aparecer essa mensagem na tela 
