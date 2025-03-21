# 1. Divisão Segura
# Crie um programa que solicite ao usuário dois números e realize a divisão do
# primeiro pelo segundo. Utilize tratamento de exceções para evitar erros de
# divisão por zero e erros de entrada inválida (como caracteres não numéricos).

def divisao_segura():
    try:
        numerador = float(input("Digite o numerador: "))
        denominador = float(input("Digite o denominador: "))
        resultado = numerador / denominador
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("Erro: divisão por zero.")
    except ValueError:
        print("Erro: entrada inválida.")
        
divisao_segura()