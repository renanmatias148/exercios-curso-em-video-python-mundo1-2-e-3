from math import factorial
print('Digite um numero para')
n1=int(input('calcular seu fatorial: '))
f=1
c= n1
print(f'calculando {n1}!= ',end="")
while c > 0:
    print(f'{c} ',end='')
    print('x'if c > 1 else  "=", end="" )
    f*= c
    c-= 1
print(f'{f}')