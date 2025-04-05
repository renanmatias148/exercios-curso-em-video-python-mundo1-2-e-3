print("LOJA SUPER BARATÃO")
print("-="*18)
menor=total=maior1=0
barato=" "
cont=0
fim="FIM DO PROGRAMA"
while True:
    produto=str(input("noome do produto: "))
    preço= int(input('preço: R$'))
    resp=str(input("quer continuar? [S/N]")).strip().upper()
    total+=preço
    cont+=1
    if preço >= 1000:
        maior1+=1
    if cont == 1:  #preço barato
        menor=preço
        barato=produto
    else:
        if preço < menor :
            menor = preço
            barato = produto
   
    if resp == "N":
        break
print(f"{fim}")
print(f"o total da compra foi R${total:.2f}")
print(f"temos {maior1} produto custando mais de R$1000.00")
print(f"o produto mais barato foi {barato} que custa R${menor:.2f}")


