fut=dict()
total=list()
fut["nome"]=str(input('nome do jogodor: '))
partidas=int(input(f"quantas partidads {fut["nome"]} jogou: "))
for p in range(1,partidas+1):
    total.append(int(input(f"quantos gols na partidas {p}: ")))
fut["gols"] =total[:]
fut["total"]=sum(total)
print("-="*30)
print(f"{fut}")
print("-="*30)
for r,n in fut.items():
    print(f"o campo {r} tem o valor {n}")
print("-="*30)
print(f"o jogador {fut['nome']} jogou {partidas} partidas")
for i,l in enumerate(total):
    print(f"na {i+1} partida, fez {l} gols")
print(f"foi um total de {fut["total"]}")