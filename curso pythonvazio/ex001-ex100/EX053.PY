fra= str(input('Digite uma frase: ')).strip().upper()
palavra= fra.split()
junto=''.join(palavra)
ivers= ''
for c in range(len(junto) -1, -1, -1):
    ivers += junto[c]
if ivers == junto:
    print('temos um palindromo!')
else:
    print('a frase digitada não é um palindromo')
    