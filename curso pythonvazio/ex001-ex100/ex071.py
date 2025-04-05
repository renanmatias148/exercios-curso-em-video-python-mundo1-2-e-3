print("-="*20)
print("bonco hash")
print('-='*20)
saque=int(input(" que valor voçe quer sacar? R$"))
ced1=50
total= saque
totalced=0
while True:
    if total>=ced1:
        total-=ced1
        totalced+=1
    else:
        if totalced>0:
            print(f"Total de {totalced} cedulas de R${ced1}")
        if ced1 == 50:
            ced1=20
        elif ced1 ==20:
            ced1=10
        elif ced1 == 10:
            ced1=1
        totalced=0
        if total==0:
            break
print("="*20)
print("volte sempre ao BANCO HASH! tenha um bom dia!")

