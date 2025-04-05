n=int(input("qauntos termos voce quer mostrar? "))
th1=0
th2=1
print(f"{th1} -> {th2}",end=" ")
cont=3
while cont <= n:
    th3= th1 + th2
    print(f'-> {th3}',end="")
    th1=th2
    th2=th3
    cont +=1
print("-> FIM!")