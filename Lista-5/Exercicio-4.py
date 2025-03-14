# 4. Contador de Vogais em uma Palavra
# Crie uma função que receba uma palavra como parâmetro e retorne a quantidade
# de vogais presentes nela. No programa principal, solicite uma palavra ao usuário e
# utilize a função para exibir o número de vogais.

def vogais(palavra):
    vogais = "aeiou"
    return sum([1 for letra in palavra if letra in vogais])

palavra = input("Digite uma palavra: ")

print(f"A palavra tem {vogais(palavra)} vogais.")