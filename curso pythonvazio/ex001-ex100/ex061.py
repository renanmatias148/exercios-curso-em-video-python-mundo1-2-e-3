primeiro=int(input('primero termo: '))
razao= int(input('razão da pa: '))
termo=primeiro
cont=1
while cont <= 10: 
    print(f'{termo} -',end=" ")
    termo += razao
    cont += 1
print('FIM!')
