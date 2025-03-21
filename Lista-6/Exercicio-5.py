# 5. Classificação de Times de Futebol
# Crie uma tupla contendo os 10 primeiros colocados de um campeonato de
# futebol. Depois, exiba:
# • Os três primeiros colocados.
# • Os últimos três colocados.
# • Os times em ordem alfabética.
# • A posição de um time específico informado pelo usuário.

def times():
    times = ("Flamengo", "Internacional", "Atlético-MG", "São Paulo", "Fluminense",
             "Palmeiras", "Santos", "Grêmio", "Sport", "Corinthians")
    print("Os três primeiros colocados são: ", end="")
    for i in range(3):
        print(times[i], end=" ")
    print()
    print("Os últimos três colocados são: ", end="")
    for i in range(7, 10):
        print(times[i], end=" ")
    print()
    print("Times em ordem alfabética: ", end="")
    for time in sorted(times):
        print(time, end=" ")
    print()
    time = input("Digite o nome de um time: ")
    if time in times:
        print(f"O time {time} está na {times.index(time) + 1}ª posição.")
    else:
        print("Time não encontrado.")
        
times()