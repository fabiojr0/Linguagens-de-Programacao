# 1. Cálculo do Fatorial
# Crie uma função que receba um número inteiro como parâmetro e retorne o seu
# fatorial. Em seguida, utilize essa função em um programa principal para calcular o
# fatorial de um número informado pelo usuário.

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    
n = int(input("Digite um número inteiro: "))

print(fatorial(n))