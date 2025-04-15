pessoas = []
soma_idades = 0

while True:
    pessoa = {}

    pessoa['nome'] = input("Nome: ").strip().capitalize()
    
    while True:
        sexo = input("Sexo: [M/F] ").strip().upper()
        if sexo in 'MF':
            pessoa['sexo'] = sexo
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    
    while True:
        try:
            idade = int(input("Idade: "))
            pessoa['idade'] = idade
            soma_idades += idade
            break
        except ValueError:
            print("Digite uma idade válida.")
    
    pessoas.append(pessoa.copy())

    while True:
        continuar = input("Quer continuar? [S/N] ").strip().upper()
        if continuar in 'SN':
            break
        print("ERRO! Responda apenas S ou N.")
    
    if continuar == 'N':
        break

print("="*40)
print(f"A) Ao todo temos {len(pessoas)} pessoas cadastradas.")

media = soma_idades / len(pessoas)
print(f"B) A média de idade é de {media:.2f} anos.")

mulheres = [p['nome'] for p in pessoas if p['sexo'] == 'F']
print("C) As mulheres cadastradas foram:", ', '.join(mulheres) if mulheres else "Nenhuma")

print("D) Lista das pessoas que estão acima da média:")
for p in pessoas:
    if p['idade'] > media:
        print(f"    nome = {p['nome']}; sexo = {p['sexo']}; idade = {p['idade']};")

print("<< ENCERRADO >>")
