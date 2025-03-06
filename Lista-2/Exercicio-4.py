# 4. Cálculo de Média e Aprovação
# Elabore um programa que solicite duas notas ao usuário e calcule a média. Em seguida,
# informe se o aluno foi:
# • Aprovado (média maior ou igual a 7)
# • Recuperação (média entre 5 e 6.9)
# • Reprovado (média abaixo de 5)

nuns = []
for i in range(2):
    nuns.append(float(input(f"Digite a {i+1}ª nota: ")))
media = sum(nuns) / len(nuns)

print(f"A média das notas é {media:.2f}")
print("Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado")

