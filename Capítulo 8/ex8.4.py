class Carro:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self, segundos):
        aceleracao = 10
        distancia = 0.5 * aceleracao * (segundos ** 2)
        self.velocidade += aceleracao * segundos
        print(f"O carro acelerou e percorreu {distancia:.2f} metros.")

    def frear(self, segundos):
        desaceleracao = 5
        distancia = 0.5 * desaceleracao * (segundos ** 2)
        self.velocidade -= desaceleracao * segundos
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"O carro freou e percorreu {distancia:.2f} metros.")

    def exibir_velocidade(self):
        print(f"Velocidade atual do carro: {self.velocidade} m/s")

meu_carro = Carro()

meu_carro.acelerar(5)
meu_carro.exibir_velocidade()
meu_carro.frear(2)
meu_carro.exibir_velocidade()
