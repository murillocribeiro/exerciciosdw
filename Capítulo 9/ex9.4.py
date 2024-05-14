class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_disponivel, valor_saque):
        self.saldo_disponivel = saldo_disponivel
        self.valor_saque = valor_saque
        super().__init__(f"Saldo insuficiente. Saldo disponível: {saldo_disponivel}, Valor do saque: {valor_saque}")

class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")

    def sacar(self, valor):
        try:
            if self.saldo < valor:
                raise SaldoInsuficienteError(self.saldo, valor)
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}")
        except SaldoInsuficienteError as e:
            print(e)

conta = ContaBancaria(100)
conta.depositar(50)
conta.sacar(30)
conta.sacar(200)
