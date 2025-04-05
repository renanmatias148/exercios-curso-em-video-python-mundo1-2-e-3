maior=0
menor=0
men=0
while True:
    idade=int(input("idade: "))
    sexo=" "
    while sexo not in "MmFf":
        sexo=str(input("sexo: [m/f] ")).upper()[0]
        print("-="*20)
    if sexo == "M":
        men+=1
    if idade >= 18:
        maior+=1
    if sexo == "F" and idade < 20:
        menor+=1
    cunt=" "
    while cunt not in "SN":
        cunt=str(input("Quer continuar? [s/n]")).strip().upper()[0]
    if cunt == "N":
        break
print(f"O total de pessoas com mais de 18 anos: {maior}")
print(f" Ao todo temos {men} homens cadastrados")
print(f"E temos {menor} mulher com menos de 20 anos")

