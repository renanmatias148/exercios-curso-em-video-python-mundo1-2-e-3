lista= []
ent=""
while True:
    n=int(input('digite um valor:'))
    lista.append(n)
    r=str(input("que continuar? [s/n]"))
    if r in "Nn":
        break
print(f"Voce digitou {len(lista)} elementos.")
lista.sort(reverse=True)
print(f"O valor em ordem descrescente sãõ {lista}")
if  lista.count(5):
    print(f"O valor 5 faz parte dessa lista")
else:
    print("O valor 5 não foi encotrado!")
