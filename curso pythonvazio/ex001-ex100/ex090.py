alunos=dict()
alunos['nome']=str(input("Nome: "))
alunos["media"]=float(input(f"Media de {alunos['nome']}: "))
print("-="*30)
print(f"- nome é igual a {alunos['nome']}")
print(f"- média e igual a {alunos['media']}")
if alunos['media'] >=7:
    print(f"-situação é igual a APROVADO")
elif alunos['media'] >=5:
    print(f"-situação é igual a RECUPERAÇÃO")
else:
    print("- situação e igual a REPROVADO")
