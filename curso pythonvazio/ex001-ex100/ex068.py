print("-="*20)
print("vamos jogar par ou impar")
print("-="*20)
total=0
resultado=""
vitorias=0
while True:
    from random import randint
    computador= randint(1,11)
    jogadorn1=int(input("digite um valor: "))
    jogador=str(input("par ou impar ? [p/i]"))
    print("-="*20)
    total=computador + jogadorn1
    if total % 2==0:
        resultado="par"
    else:
        resultado="impar"
    print(f"Voçe jogou {jogadorn1} e o computador {computador}. total de {total} deu {resultado}")
    if jogador == resultado:
        print("-="*20)
        print("VOÇE VENCEU!")
        print("vamos jogar novamente...")
        vitorias+=1
    else:
        print("-="*20)
        print("VOÇE PERDEU!")
        if jogador != resultado:
            break
print("-="*20)
print(f"GAME OVER! voçe venceu {vitorias} vezes.")
