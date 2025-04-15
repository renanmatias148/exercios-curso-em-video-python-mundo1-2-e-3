time = []  # Lista principal que guarda todos os jogadores

while True:
    jogador = {}
    partidas = []

    jogador['nome'] = input('Nome do Jogador: ')
    total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for i in range(total_partidas):
        gols = int(input(f'  Quantos gols na partida {i + 1}? '))
        partidas.append(gols)

    jogador['gols'] = partidas[:]  # Cópia da lista
    jogador['total'] = sum(partidas)  # Soma total de gols
    time.append(jogador.copy())  # Cópia do dicionário

    continuar = input('Quer continuar? [S/N] ').strip().lower()
    if continuar == 'n':
        break

# Mostrar o cabeçalho da tabela
print('=' * 50)
print(f'{"cod":<4} {"nome":<10} {"gols":<20} {"total":<5}')
print('-' * 50)

for i, jogador in enumerate(time):
    print(f'{i:<4} {jogador["nome"]:<10} {str(jogador["gols"]):<20} {jogador["total"]:<5}')

# Consultar dados dos jogadores
while True:
    print('-' * 50)
    cod = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if cod == 999:
        break
    if cod >= len(time):
        print(f'ERRO! Não existe jogador com código {cod}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[cod]["nome"]}:')
        for i, g in enumerate(time[cod]["gols"]):
            print(f'   No jogo {i + 1} fez {g} gols.')
