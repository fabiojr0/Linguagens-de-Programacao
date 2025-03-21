# 2. Contagem de Caracteres em uma Palavra
# Escreva um programa que solicite ao usuário uma palavra e utilize um dicionário
# para armazenar a contagem de cada caractere presente na palavra. Exiba o
# dicionário ao final.

def caracteres():
    palavra = input("Digite uma palavra: ")
    contagem = {}
    for letra in palavra:
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1
    print(contagem)
    
caracteres()