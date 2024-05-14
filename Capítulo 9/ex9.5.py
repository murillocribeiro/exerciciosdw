def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    
    except FileNotFoundError:
        print("O arquivo '{}' não foi encontrado.".format(nome_arquivo))
    
    except PermissionError:
        print("Não foi possível ler o arquivo '{}'.".format(nome_arquivo))

nome_arquivo = "murillo.txt"
ler_arquivo(nome_arquivo)
