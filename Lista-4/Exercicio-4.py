# 4. Inverter a Lista
# Escreva um programa que leia uma lista de palavras e exiba essa lista na ordem
# inversa.

palavras = input("Digite uma lista de palavras separadas por espaço ou vírgula: ")  

lista_palavras = palavras.replace(",", " ").split()

lista_palavras.reverse()

print(f"A lista de palavras invertida é: {lista_palavras}")