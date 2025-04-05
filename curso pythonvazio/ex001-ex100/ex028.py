from random import randint
computador= randint(1,6)
print('vou pensa em um numero ente 1 a 6, tente adivinhar..')
jogador=int(input("Em que numero pensei? "))
print("processando....")
if jogador == computador:
    print(" Parabens voce adivinho.bom palpite")
else:
    print("Ganhei, pensei no numero {} e nao no {} tente da proxima...rsrsrs".format(computador,jogador))

    