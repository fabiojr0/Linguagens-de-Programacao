# 4. Processamento de Strings
# Peça ao usuário para digitar uma frase e implemente funções para:
# • Contar quantas vezes cada vogal aparece na frase.
# • Exibir a frase ao contrário.
# • Substituir todos os espaços por -.

def processar_frase():
    frase = input("Digite uma frase: ")
    vogais = "aeiou"
    for vogal in vogais:
        print(f"A vogal {vogal} aparece {frase.lower().count(vogal)} vezes.")
    print(f"Frase ao contrário: {frase[::-1]}")
    print(f"Frase com espaços substituídos por -: {frase.replace(' ', '-')}")
    
processar_frase()

# 5. Manipulação de Listas e Strings
# Solicite ao usuário que insira uma lista de palavras separadas por espaço. Em seguida,
# exiba:
# • A lista ordenada alfabeticamente.
# • O número total de palavras.
# • As palavras convertidas para maiúsculas.

def manipular_lista():
    palavras = input("Digite uma lista de palavras separadas por espaço: ").split()
    palavras.sort()
    print("Lista ordenada alfabeticamente:"," ".join(palavras))
    
    print(f"Número total de palavras: {len(palavras)}")
    
    print("Palavras convertidas para maiúsculas:", end=" ")
    
    for palavra in palavras:
        print(palavra.upper(), end=" ")
        
    print()
    
manipular_lista()

# 6. Tratamento de Exceções
# Crie um programa que solicite ao usuário dois números e tente dividir o primeiro pelo
# segundo. O programa deve capturar exceções como ZeroDivisionError e ValueError
# e exibir mensagens apropriadas.

def tratar_excecoes():
    while True:
        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            print(f"Resultado: {numero1 / numero2}")
            break
        except ZeroDivisionError:
            print("Erro: divisão por zero.")
        except ValueError:
            print("Erro: entrada inválida.")
            
tratar_excecoes()
    