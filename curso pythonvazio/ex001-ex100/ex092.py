clt=dict()
from datetime import datetime
clt['nome']=str(input("Nome: "))
clt['nacimento']=int(input("ano de nascimento: "))
clt['cart']=int(input('Carteira de trabalho: (0 não tem)'))
if clt['cart'] != 0:
    clt["cont"]=int(input('ano de contratação: '))
    clt["salario"]=float(input("salario: R$"))
    clt["aposentadoria"]=clt['nacimento']+((clt['cont'] + 35) - datetime.now().year)
print("-="*30)
print(f"- O nome tem valor {clt['nome']}")
print(f"a idade tem o valor {clt["nacimento"]}")
print(f"o cpts tem o valor {clt['cart']}")
if clt["cart"] != 0:
    print(f"contratação tem o valor {clt['cont']}")
    print(f"o salario tem valor de R${clt['salario']}")
    print(f"A aposentadoria tem o valor de {clt['aposentadoria']}")
