# 2. Maior Número
# Faça um programa que peça dois números ao usuário e exiba o maior deles. Caso os números
# sejam iguais, exiba uma mensagem informando essa condição.

nuns = []
for i in range(2):
    nuns.append(float(input(f"Digite o {i+1}º número: ")))
maior = max(nuns)
print(f"O maior número é {maior}")

