import random
pn= str(input('primeiro nome:'))
sn= str(input('segundo nome:'))
tn= str(input('terceiro nome:'))
qn= str(input('quarto nome:'))
aluno= (pn,sn,tn,qn)
escolhido= random.choice (aluno)
print("o aluno escolhido e {}".format(escolhido))
