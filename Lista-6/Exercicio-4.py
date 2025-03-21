# 4. Nomes de Alunos e Notas
# Crie uma tupla que armazene o nome de cinco alunos e suas respectivas notas
# (ex: ('Ana', 8.5, 'Carlos', 7.0, 'Beatriz', 9.2, 'Daniel', 6.8, 'Eduarda', 8.0)). Depois, exiba
# apenas os nomes dos alunos e, em seguida, apenas as notas.

def alunos_notas():
    alunos = ("Ana", 8.5, "Carlos", 7.0, "Beatriz", 9.2, "Daniel", 6.8, "Eduarda", 8.0)
    print("Nomes dos alunos: ", end="")
    for i in range(0, len(alunos), 2):
        print(alunos[i], end=" ")
    print()
    print("Notas dos alunos: ", end="")
    for i in range(1, len(alunos), 2):
        print(alunos[i], end=" ")
    print()
    
alunos_notas()