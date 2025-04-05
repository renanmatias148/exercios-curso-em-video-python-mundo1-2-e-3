nota1= float(input('primera nota: '))
nota2= float(input('segunda nota: '))

m= (nota1 + nota2) /2

print("Tirando {} e {}, a media do aluno é {}".format(nota1, nota2, m))
      
if 7> m >= 5:
    print("O aluno esta de {}RECUPERAÇÃO{}".format("\033[33m","\033[m"))
elif m < 5:
    print("O aluno esta {}REPROVADO{}".format("\033[31m","\033[m"))
else:
    print("O aluno esta \033[32m APROVADO\033[m")