num= tent = soma =0
tent=0
v1=999
soma=0
n1=int(input("digite um numero [999 para parar]:"))
while n1 != 999:
    tent += 1
    soma += n1
    n1=int(input("digite um numero [999 para parar]:"))
print(f'Voce digitou {tent} numeros e a soma entre ele foi {soma}')