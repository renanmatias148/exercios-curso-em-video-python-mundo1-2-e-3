import random
lista=[1,2,3,4,5,6,7,8,9,10]
def numero6():
    print("Analisando os valores passados...")
    n1=random.sample(lista,6)
    print(f"{n1} foram informados {len(n1)} valores ao todo.")
    maior=max()
    print(f"o maior valor informa foi {max(n1)}")
    print("-="*30)
    return max
numero6(6)