class TrianguloError(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def tipo_triangulo(self):
        try:
            if self.lado1 <= 0 or self.lado2 <= 0 or self.lado3 <= 0:
                raise TrianguloError("Os lados do triângulo devem ser positivos.")
            if self.lado1 + self.lado2 <= self.lado3 or self.lado1 + self.lado3 <= self.lado2 or self.lado2 + self.lado3 <= self.lado1:
                raise TrianguloError("Os lados do triângulo não formam um triângulo válido.")
            if self.lado1 == self.lado2 == self.lado3:
                return "Triângulo Equilátero"
            elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
                return "Triângulo Isósceles"
            else:
                return "Triângulo Escaleno"
        except TrianguloError as e:
            return str(e)
        
try:
    t1 = Triangulo(3, 4, 5)
    print(t1.tipo_triangulo())

    t2 = Triangulo(1, 1, 3)
    print(t2.tipo_triangulo())
except TrianguloError as e:
    print(e)
