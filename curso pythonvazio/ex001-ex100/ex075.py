n1=int(input('Digite um numero: '))
n2=int(input('Digite outro numero: '))
n3=int(input('Digite mais um numero: '))
n4=int(input("Digite o ultimo numero: "))
valores=n1,n2,n3,n4
print(f"Voçe digitou os valores {valores}")
print(f"O valor 9 apareceu {valores.count(9)} vezes")
print(f"O valor 3 aparceu na {valores.index(3)}° posição")
print(f"Os valores pares digitados foram ", end='')
for n in valores:
    if n %2 ==0:
        print(n,end=" ")


