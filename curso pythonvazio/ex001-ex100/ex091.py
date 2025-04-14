from random import randint
from operator import itemgetter
jogadores={'jogador1':randint(1,6),
           'jogador2':randint(1,6),
           'jogador3':randint(1,6),
           'jogador4':randint(1,6)}
print('VALORES SORTEADOS')
for k,v in jogadores.items():
    print(f"{k} tirou {v} no dado.")
print("-="*30)
print(f"=={"RANKING DOS JOGADORES":^}==")
rank=sorted(jogadores.items(),key=itemgetter(1),reverse=True)
for i,v in enumerate(rank):
    print(f"{i+1}° lugar: {v[0]} com {v[1]}")
