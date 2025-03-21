# 2. Operações Matemáticas com Números em uma Tupla
# Solicite ao usuário quatro números inteiros e armazene-os em uma tupla. Em
# seguida, exiba:
# • Quantas vezes o número 9 apareceu na tupla.
# • Em que posição foi digitado o primeiro número 3 (caso exista).
# • Os números pares contidos na tupla.

def tupla():
    numeros = tuple([int(x) for x in input("Digite 4 números inteiros separados por espaço: ").split()])
    print(f"O número 9 apareceu {numeros.count(9)} vezes na tupla.")
    if 3 in numeros:
        print(f"O primeiro número 3 foi digitado na posição {numeros.index(3) + 1}.")
    print("Os números pares contidos na tupla são: ", end="")
    for n in numeros:
        if n % 2 == 0:
            print(n, end=" ")
    print()
            
tupla()