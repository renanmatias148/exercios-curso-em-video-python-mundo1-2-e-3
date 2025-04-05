from datetime import date
atual= date.today().year
totalma= 0
tatalmen= 0
for n in range (1,8):
    nasc=int(input(f"em que ano {n}° pessoa nasceu? "))
    idade= atual- nasc
    if idade >= 18:
        totalma += 1
    else:
        tatalmen +=1
print(f"{tatalmen} pessoas sao menores de idade")
print(f"{totalma} pessoas sao maiores de idade")
