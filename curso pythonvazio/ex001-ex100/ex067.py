
while True:
    print("-="*20)
    n1=int(input('qual valor voçe que a tabuada?'))
    if n1 < 0:
        break
    for c in range(1,11):
        print(f"{n1} x {c} = {n1*c}")
    

