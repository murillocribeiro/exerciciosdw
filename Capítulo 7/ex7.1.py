def exibir_conteudo_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do arquivo:")
            print(conteudo)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def main():
    nome_arquivo = input("Digite o nome do arquivo: ")
    exibir_conteudo_arquivo(nome_arquivo)

if __name__ == "__main__":
    main()
