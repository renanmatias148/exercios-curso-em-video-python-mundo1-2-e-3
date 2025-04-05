a=int(input('primeiro valor: '))
b=int(input('segundo valor: '))
c=int(input('terceiro valor: '))
#verefique o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verefique o maior
maior = a
if b > a and b > c:
    menor = b
if c > a and c > b:
    menor = c
print('o menor numero {}'.format(menor))
print("o maior numero {}".format(maior))