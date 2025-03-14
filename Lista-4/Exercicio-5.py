# 5. Contar Ocorrências de um Elemento
# Escreva um programa que peça ao usuário para inserir uma lista de números e um
# número específico. O programa deve contar quantas vezes esse número aparece
# na lista.

numeros = input("Digite uma lista de números inteiros separados por espaço ou vírgula: ")

lista_numeros = list(map(int, numeros.replace(",", " ").split()))

numero = int(input("Digite um número para contar as ocorrências na lista: "))

ocorrencias = lista_numeros.count(numero)

print(f"O número {numero} aparece {ocorrencias} vezes na lista.")