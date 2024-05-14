import os

nome_diretorio = "murillo"
nome_arquivo = "murillo.txt"

if not os.path.exists(nome_diretorio):

    os.makedirs(nome_diretorio)

caminho_arquivo = os.path.join(nome_diretorio, nome_arquivo)
with open(caminho_arquivo, "w") as arquivo:
    arquivo.write("Lista de Exercicios de Python do Ricardo Marochio")

print("Diretório e arquivo criados com sucesso!")
