# 3. Remover Duplicatas
# Escreva um programa que leia uma lista de números e remova os valores
# duplicados, mantendo a ordem original.

numeros = input("Digite uma lista de números inteiros separados por espaço ou vírgula: ")

lista_numeros = list(map(int, numeros.replace(",", " ").split()))

lista_sem_duplicatas = list(dict.fromkeys(lista_numeros))

print(f"A lista sem duplicatas é: {lista_sem_duplicatas}")