# 1. Cálculo da Área do Círculo
# Escreva um programa que peça ao usuário o valor do raio de um círculo e calcule sua área.
# Use a fórmula:
# Dica: Use math.pi para obter o valor de π.

raio = float(input("Digite um raio de um círculo: "))
area = math.pi * (raio ** 2)
print(f"A área do círculo é {area:.2f}")