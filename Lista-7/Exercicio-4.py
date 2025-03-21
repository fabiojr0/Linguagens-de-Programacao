# 4. Estatísticas de um Texto
# Peça ao usuário para inserir uma frase. Utilize um dicionário para armazenar a
# contagem de palavras, ou seja, a chave será a palavra e o valor será o número de
# vezes que ela aparece na frase. Exiba o dicionário ao final.

def estatisticas():
    frase = input("Digite uma frase: ")
    contagem = {}
    for palavra in frase.split():
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    print(contagem)
    
estatisticas()