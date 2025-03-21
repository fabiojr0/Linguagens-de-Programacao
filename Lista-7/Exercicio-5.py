# 5. Catálogo de Produtos
# Crie um dicionário onde as chaves representem códigos de produtos e os valores
# sejam tuplas contendo o nome do produto e seu preço. Permita que o usuário
# informe um código para buscar o nome e o preço do produto correspondente.

def catalogo():
    produtos = {
        1: ("Camiseta", 29.90),
        2: ("Calça", 59.90),
        3: ("Tênis", 99.90)
    }
    codigo = int(input("Digite o código do produto: "))
    if codigo in produtos:
        nome, preco = produtos[codigo]
        print(f"Nome: {nome}\nPreço: R${preco:.2f}")
    else:
        print("Produto não encontrado.")
        
catalogo()