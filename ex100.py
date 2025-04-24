# Importando funções necessárias de bibliotecas externas
from random import randint   # Para gerar números aleatórios
from time import sleep       # Para fazer o programa "dormir" por alguns segundos

# Função que sorteia 5 números aleatórios e coloca na lista
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):  # Vai repetir 5 vezes
        n = randint(1, 10)    # Gera um número aleatório entre 1 e 10
        lista.append(n)       # Adiciona esse número na lista
        print(f'{n} ', end='', flush=True)  # Mostra o número sorteado na tela
        sleep(0.3)            # Espera 0.3 segundos antes de continuar
    print('PRONTO!')          # Mensagem final depois de sortear tudo

# Função que soma apenas os números pares da lista
def somaPar(lista):
    soma = 0                 # Inicializa a variável soma com zero
    for valor in lista:      # Percorre cada valor da lista
        if valor % 2 == 0:   # Verifica se o valor é par
            soma += valor    # Se for par, soma com o total
    print(f'Somando os valores pares de {lista}, temos {soma}')  # Mostra o resultado

# Programa principal
números = list()             # Cria uma lista vazia chamada números
sorteia(números)            # Chama a função sorteia passando a lista
somaPar(números)            # Chama a função somaPar passando a mesma lista
