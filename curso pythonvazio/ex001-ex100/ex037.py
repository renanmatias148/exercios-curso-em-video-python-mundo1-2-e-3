num=int(input("digite um numero inteiro: "))
print("escolha uma das bases para conversão:")
print('[1} Converte para binario')
print('[2] Converte para octal')
print('[3] Converte para hexadecimal')
opçao= int(input('sua opção: '))
bin_1=bin(num)
oct_2= oct(num)
hex_3= hex(num)
if opçao == 1:
    print("{} convertido para BINARIO é igual a {}".format(num,bin_1[2:]))
elif opçao == 2:
    print("{} convertido para OCTAL é igual a {}".format(num,oct_2[2:]))
elif opçao == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(num,hex_3[2:]))
