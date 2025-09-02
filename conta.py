class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def exibir_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R${self.saldo:.2f}")

# Teste simples
if __name__ == "__main__":
    conta = ContaBancaria("Victor Gabriel")
    conta.exibir_saldo()