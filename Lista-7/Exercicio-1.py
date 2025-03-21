# 1. Cadastro de Alunos
# Crie um programa que permita cadastrar alunos em um dicionário. O programa
# deve solicitar o nome e a nota do aluno e armazená-los como chave e valor no
# dicionário. Após a inserção de pelo menos 3 alunos, exiba a lista de alunos e suas
# respectivas notas.

def alunos():
    alunos = {}
    for _ in range(3):
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        alunos[nome] = nota
    print("Lista de alunos e suas respectivas notas:")
    for nome, nota in alunos.items():
        print(f"{nome}: {nota}")
        
alunos()