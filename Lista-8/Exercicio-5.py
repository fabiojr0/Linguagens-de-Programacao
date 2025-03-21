# 5. Operações Bancárias com Tratamento de Erros
# Crie um programa que simule um sistema bancário simples. O saldo inicial do
# usuário é de R$ 1000,00. O programa deve permitir que o usuário insira um valor
# para saque e, caso o valor solicitado seja maior que o saldo disponível, uma
# exceção personalizada deve ser lançada informando que o saldo é insuficiente.

class SaldoInsuficiente(Exception):
    def __init__(self, saldo, valor):
        self.saldo = saldo
        self.valor = valor
        super().__init__(f"Saldo insuficiente. Saldo atual: R${saldo:.2f}, valor do saque: R${valor:.2f}")
        
def saque(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficiente(saldo, valor)
    return saldo - valor

saldo = 1000.00

while True:
    try:
        valor = float(input("Digite o valor do saque: "))
        saldo = saque(saldo, valor)
        print(f"Saque realizado com sucesso. Saldo atual: R${saldo:.2f}")
        break
    except ValueError:
        print("Erro: entrada inválida.")
    except SaldoInsuficiente as erro:
        print(erro)
