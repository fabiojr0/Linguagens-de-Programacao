# 4. Acesso a Elementos de uma Lista
# Crie uma lista com cinco números e permita que o usuário informe um índice para
# acessar um valor da lista. Utilize tratamento de exceções para evitar erros caso o
# usuário digite um índice inválido.

def acessar_lista():
    lista = [1, 2, 3, 4, 5]
    while True:
        try:
            indice = int(input("Digite um índice para acessar um valor da lista: "))
            print(f"Valor: {lista[indice]}")
            break
        except IndexError:
            print("Erro: índice inválido.")
        except ValueError:
            print("Erro: entrada inválida.")
            
acessar_lista()