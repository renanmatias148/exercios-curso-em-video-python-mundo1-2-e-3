from time import sleep
n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
opçao=0
while opçao != 5 :
    print("""
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novo numeros
    [5] sair do programa """)
    opçao=int(input('Qual e a sua opção? '))
    if opçao == 1:
        soma= n1+n2
        print(f"A soma {n1} + {n2} é {soma}")
    elif opçao == 2:
        mult= n1*n2
        print(f"O resultado de {n1} x {n2} é {mult}")
    elif opçao == 3:
        if n1 > n2:
            maior=n1
        else:
            maior=n2
        print(f'o maior è {maior}')
    elif opçao == 4:
        print('informe novo numeros')
        n1=int(input('primeiro valor: '))
        n2=int(input('segundo valor: '))
    elif opçao == 5:
        print('finalizando...')
    else:
        print('opção invalida.tente novamente')
    print('=-='*10)
    sleep(2)
print("fim do programa!volte sempre")
