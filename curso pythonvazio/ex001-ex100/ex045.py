from random import randint
from time import sleep
itens=('pedra','papel','tesoura')
computador=randint(0,2)
print('''{:=^4}
    [0]PEDRA
    [1]PAPEL
    [2]TESOURA'''.format("OPÇÕES DE JOGADA:"))

jogador=int(input('Qual e sua jogada? '))
print('jo')
sleep(1)
print('ke')
sleep(1)
print('po !!!')
print("=="*12)
print('COMPUTADOR JOGOU {}'.format(itens[computador]))
print('JOGADOR JOGOU {}'.format(itens[jogador]))
if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador ==2:
        print('COMPUTADOR VENCEU')

elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('COMPURADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador ==2:
        print('JOGADOR VENCEU')

elif computador ==2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador ==2:
        print('EMPATE')