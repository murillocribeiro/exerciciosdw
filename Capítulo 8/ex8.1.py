class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

pessoa1 = Pessoa("Murillo", 21)
pessoa2 = Pessoa("Pedro Henrique", 7)

pessoa1.mostrar_dados()
pessoa2.mostrar_dados()
