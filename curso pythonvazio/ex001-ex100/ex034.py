sal= float(input("qual salario do funcionario? R$"))
aum= sal + (sal*15/100)
aum10= sal + (sal*10/100)
if sal >= 1250:
    print("Quem ganhava R${} passa a ganhar R${:.2f}".format(sal,aum10))
else:
    print('Quem ganhava R${} passa a ganhar R${:.2f}'.format(sal,aum))
    
