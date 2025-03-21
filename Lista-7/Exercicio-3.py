# 3. Dicionário de Tradução
# Crie um dicionário que contenha algumas palavras em português como chave e
# suas respectivas traduções para inglês como valor. Permita que o usuário digite
# uma palavra em português e retorne sua tradução. Caso a palavra não esteja no
# dicionário, exiba uma mensagem informando que a tradução não foi encontrada.

def traducao():
    dicionario = {
        "cachorro": "dog",
        "gato": "cat",
        "rato": "mouse",
        "elefante": "elephant",
        "leão": "lion",
        "tigre": "tiger",
        "girafa": "giraffe",
        "macaco": "monkey",
        "pássaro": "bird",
    }
    palavra = input("Digite uma palavra em português: ")
    if palavra in dicionario:
        print(f"A tradução de {palavra} é {dicionario[palavra]}.")
    else:
        print("Tradução não encontrada.")
        
traducao()