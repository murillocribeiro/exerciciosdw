num_alunos = int(input("Quantos alunos você deseja cadastrar? "))

alunos_notas = {}

for i in range(num_alunos):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    alunos_notas[nome] = nota

alunos_aprovados = {nome: nota for nome, nota in alunos_notas.items() if nota >= 7}

print("Alunos aprovados:")
print(alunos_aprovados)
