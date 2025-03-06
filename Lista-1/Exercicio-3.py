# 3. Média de Três Números
# Crie um programa que receba três números do usuário e calcule a média aritmética deles.
# A fórmula é:

nuns = []
for i in range(3):
    nuns.append(float(input(f"Digite o {i+1}º número: ")))

media = sum(nuns) / len(nuns)
print(f"A média dos números é {media:.2f}")