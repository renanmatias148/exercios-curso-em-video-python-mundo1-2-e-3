frase = str (input("digite uma frase:")).upper().strip()
print("A letra A apareceu {} vezes na frase".format((frase.count("A"))))
print("A primeira letra  A aparecu na posiçao {}".format((frase.find("A")+1)))
print("A ultima letra A apareceu na posiçao {}".format((frase.rfind("A")+1)))

