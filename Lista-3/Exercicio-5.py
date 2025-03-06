# 5. Sequência de Fibonacci
# Escreva um programa que peça ao usuário um número N e exiba os N primeiros termos da
# Sequência de Fibonacci.
# Obs: A sequência de Fibonacci começa com 0 e 1, e cada termo seguinte é a soma dos dois
# anteriores:

num = int(input("Digite um número inteiro positivo: "))

a, b = 0, 1
for i in range(num):
    print(a)
    a, b = b, a+b