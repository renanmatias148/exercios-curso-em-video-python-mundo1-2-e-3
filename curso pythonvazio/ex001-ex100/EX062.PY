primeiro=int(input('primero termo: '))
razao= int(input('razão da pa: '))
termo=primeiro
cont=1
total=0
mais=10
while mais != 0:
    total += mais 
    while cont <= total: 
        print(f'{termo} -',end=" ")
        termo += razao
        cont += 1
    print("PAUSA")
    mais=int(input('quantos termos voce quer meostrarf a mais? '))
print(f'progresao finalizada com {total} termos mostrados!')