num= int(input("Digite um numero: "))
tot=0
for c in range (1,num+1):
    if num % c == 0:
        print('\033[32m',end=" ")
        tot += 1
    else:
        print('\033[31m',end=" ")
    print(f"{c}", end=" ""\033[m")
print('\n'f"O nomero {num} foi divisivel {tot} vezes")
if tot == 2:
    print("Por isso ele É PRIMO")
else:
    print("Por isso ele NÃO É PRIMO")