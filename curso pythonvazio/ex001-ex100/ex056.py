velho=0
novo=0
menor=0
nome=0
femenino= 0
media=0
for dados in range (1,5):
    print(f"==== {dados}° PESSOA ====")
    nome=str(input("Nome: "))
    idade=int(input("Idade: "))
    sexo= str(input("Sexo[M/F]: "))
    media += idade
    if dados == 1 and sexo == "m":  #idade da pessoa mas velha
        velho= dados
        novo= dados
    else:
        if idade > velho and sexo == "m":
            velho = idade
        if idade < novo and sexo == "m":
            novo = idade
    if dados ==1: # nome da pessoa mas velha
        nome = dados
    else:
        if nome == velho:
           velho += nome
    if idade < 20 and sexo == "f": #Mulheres com menos de 20 anos
        femenino += 1
mediade = media  / 4
print(f" A media de idade do grupo e {mediade} anos.")
print(f"O homem mais velho tem {velho} anos e se chama {nome}.")
print(f"Ao todo são {femenino} mulheres com menos de 20 anos.")