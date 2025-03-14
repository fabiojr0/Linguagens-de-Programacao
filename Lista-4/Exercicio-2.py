# 2. Encontrar o Maior e o Menor Número
# Escreva um programa que leia uma lista de números digitados pelo usuário e
# determine o maior e o menor número presentes na lista.

numeros = input("Digite uma lista de números inteiros separados por espaço ou vírgula: ")

lista_numeros = list(map(int, numeros.replace(",", " ").split()))

maior = max(lista_numeros)
menor = min(lista_numeros)

print(f"O maior número da lista é: {maior}")
print(f"O menor número da lista é: {menor}")
