print('{:=^40}'.format("LOJA RENAN"))
preço= float(input("preco da compra: R$"))
print("""Formas de Pagamento
      [1] á vista/ cheque
      [2] á vista no cartão
      [3] 2x no cartão 
      [4] 3x ou mais no cartão""")
opção= int(input("Qual forma de pagamento? "))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    tota = preço  - (preço * 5 / 100)
elif opção == 3:
    total = preço / 2
    print("Sua compra será parcelada em 2x de R${}".format(total))
elif opção == 4:
    parcela= int(input('Quantas parcela? '))
    total = preço + (preço * 20/100)
    toparc = total / parcela
    print("Sua compra parcelada em {}x de R${} COM JUROS ".format(parcela,toparc))
else:
    print("Opçãp invalida,tente novamente.")


print("Sua compra de R${} vai custa R${}".format(preço, total))