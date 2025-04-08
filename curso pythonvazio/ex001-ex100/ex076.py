lista=("lapis",1.75,
    "borracha",2,
    "caderno",15,
    "estojo",25,
    "Trasferidor",4.20,
    "compasso",9.99,
    "ochila",120.32,
    "caneta",22.30,
    "livro",34.90)
print("-"*39)
print(f'{"listagem de preço":^39}')
print("-"*39)
for pos in range(0,len(lista)):
    if pos % 2 ==0:
        print(f"{lista[pos]:.<30}",end="")
    else:
        print(f"R${lista[pos]:>7}")


    
