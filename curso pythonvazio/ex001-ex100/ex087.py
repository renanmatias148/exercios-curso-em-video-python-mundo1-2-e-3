matrix=[[0],[0],[0]],[[0],[0],[0]],[[0],[0],[0]]
sompar=tercol= maior=0
for l in range(0,3):
    for c in range(0,3):
        matrix[l][c]=int(input(f"digite um numero para posição [{l},{c}]"))
print("-="*30)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matrix[l][c]:^5}]",end="")
        if matrix [l][c] %2==0:
            sompar+=matrix[l][c]
    print()
print(f"A soma dos valores pares é {sompar}")
for l in range(0,3):
    tercol+=matrix[l][2]
print(f"A soma dos valores da terceira coluna é{tercol}")
for c in range(0,3):
    if c==0:
        maior+=matrix[1][c]
    elif matrix[1][c]> maior:
        maior=matrix[1][c]
print(f"O maior valor da segunda linha é {maior}")