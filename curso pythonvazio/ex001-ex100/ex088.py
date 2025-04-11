from random import randint
from time import sleep
jogos=list()
lista=[]
print("-="*30)
print(f"{"jogos da mega sena":^}")
print("-="*30)
palpítes=int(input("Quantos palpites deseja  ver? "))
tot=0
while tot <= palpítes:
    cont=0
    while True:
        num=randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont>=6:
             break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print("-="*3, f"SORTEANDO {palpítes} JOGOS", "-="*3)
for i,l in enumerate(jogos):
    print(f'JOGO {i+1}: {l}')
    sleep(2)
print("=-"*5,"<BOA SORTE>","-="*5)