from random import randint
computador= randint(0,10)
print('vou pensa em um numero ente 0 a 10, tente adivinhar..')
jogador=int(input("qual seu papite ? "))
tent=0
while jogador != computador:
    print("tente mais uma vez")
    jogador=int(input('qual é seu papite? '))
    tent += 1
print(f'acertou com {tent} tentativas. parabens!')
    
    