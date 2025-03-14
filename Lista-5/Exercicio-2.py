# 2. Verificação de Número Primo
# Crie uma função que receba um número inteiro e retorne True se for primo e False
# caso contrário. No programa principal, solicite um número ao usuário e utilize a
# função para verificar se ele é primo.

def primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Digite um número inteiro: "))

print(primo(n))