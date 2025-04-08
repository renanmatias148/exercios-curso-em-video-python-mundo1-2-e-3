import random
numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,15
ale= random.sample(numeros, k=5)
print(f"Os valores sorteados foram: {ale}")
print(f"O maior valor sorteado foi {max(ale)}")
print(f"O menor valor sorteado foi {min(ale)}")

