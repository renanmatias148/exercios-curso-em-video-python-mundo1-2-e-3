casa= float(input("valor da casa: R$"))
salario= float(input("qual eo seu salario? R$"))
prestaçao=int(input('E quantos anos deseja pagar'))
parcela= casa / (prestaçao*12)
minimo= salario * 30/100
print("Para pagar a casa de R${:.2f} em {}anos a prestaçao sera de R${:.2f}".format(casa,prestaçao,parcela))
if parcela <= minimo:
    print("Empretimo concedido com SUCESSO")
else:
    print("Emprestimo NEGADO/033")
