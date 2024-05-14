import os

def renomear_arquivo(nome_arquivo):
    nome, extensao = os.path.splitext(nome_arquivo)

    novo_nome = f"{nome}_renomeado{extensao}"

    os.rename(nome_arquivo, novo_nome)

    print(f"Arquivo renomeado para '{novo_nome}'.")

def main():
    nome_arquivo = input("Digite o nome do arquivo: ")

    renomear_arquivo(nome_arquivo)

if __name__ == "__main__":
    main()
