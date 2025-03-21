# 2. Abertura Segura de Arquivo
# Escreva um programa que solicite ao usuário o nome de um arquivo para leitura. O
# programa deve tentar abrir o arquivo e exibir seu conteúdo. Utilize tratamento de
# exceções para lidar com a ausência do arquivo e outros possíveis erros.

def abrir_arquivo():
    try:
        nome_arquivo = input("Digite o nome do arquivo: ")
        with open(nome_arquivo, "r") as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
    except Exception as erro:
        print(f"Erro: {erro}")
        
abrir_arquivo()