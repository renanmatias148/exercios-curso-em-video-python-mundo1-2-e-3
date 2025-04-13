# Lista que vai armazenar os dados dos alunos
ficha = []

# Loop principal para cadastro de alunos
while True:
    nome = input('Nome: ')  # Pede o nome do aluno
    notas = [float(input('Nota 1: ')), float(input('Nota 2: '))]  # Recebe as duas notas e guarda numa lista
    media = sum(notas) / 2  # Calcula a média das duas notas
    ficha.append([nome, notas, media])  # Adiciona tudo à ficha: nome, lista de notas e média

    # Pergunta se quer continuar. Se digitar 'n', sai do laço
    if input('Quer continuar? [S/N] ').strip().lower() == 'n':
        break

# Exibe a lista de alunos com suas médias
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')  # Cabeçalho formatado
print('-' * 26)

# Mostra o índice, nome e média de cada aluno
for i, aluno in enumerate(ficha):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')  # i = número do aluno, aluno[0] = nome, aluno[2] = média

# Loop para consultar as notas completas de um aluno
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    # Se digitar 999, o programa encerra
    if opc == 999:
        print('FINALIZANDO...')
        break

    # Verifica se o número digitado é válido
    if 0 <= opc < len(ficha):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')  # Mostra nome e lista de notas

# Mensagem final
print('<<< VOLTE SEMPRE >>>')
