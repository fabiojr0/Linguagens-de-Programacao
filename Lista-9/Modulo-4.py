# 10. Geradores
# Implemente um gerador chamado contar_pares(n) que gera números pares até n. No
# programa principal, utilize for para exibir os números pares até um valor inserido pelo
# usuário.

def contar_pares(n):
    for i in range(2, n + 1, 2):
        yield i
        
n = int(input("Digite um número: "))
for i in contar_pares(n):
    print(i, end=" ")
print()

# 11. Iteradores
# Crie uma classe Contador que implemente um iterador que conta de 1 até n. No
# programa principal, percorra os valores utilizando for.

class Contador:
    def __init__(self, n):
        self.n = n
        self.i = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        self.i += 1
        if self.i <= self.n:
            return self.i
        else:
            raise StopIteration
        
n = int(input("Digite um número: "))

for i in Contador(n):
    print(i, end=" ")
print()

# 12. Closures
# Implemente uma função multiplicador(fator) que recebe um número fator e
# retorna uma função que multiplica qualquer número por esse fator. Teste a função no
# programa principal.

def multiplicador(fator):
    def multiplicar(n):
        return n * fator
    return multiplicar

fator = float(input("Digite um fator: "))

multiplicar = multiplicador(fator)

n = float(input("Digite um número: "))

print(f"Resultado: {multiplicar(n)}")

# 13. Processamento de Arquivos de Texto
# Crie um programa que leia um arquivo chamado dados.txt, conte quantas linhas ele
# possui e exiba o conteúdo na tela.

with open("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    print(f"O arquivo possui {len(linhas)} linhas.")
    for linha in linhas:
        print(linha, end="")

# 14. Processamento de Arquivos Binários
# Escreva um programa que crie um arquivo binário dados.bin e grave uma lista de
# números inteiros nele. Em seguida, abra o arquivo e exiba os números armazenados.

numeros = [1, 2, 3, 4, 5]

with open("dados.bin", "wb") as arquivo:
    for numero in numeros:
        arquivo.write(numero.to_bytes(4, "little"))
        
with open("dados.bin", "rb") as arquivo:
    while True:
        byte = arquivo.read(4)
        if not byte:
            break
        print(int.from_bytes(byte, "little"))
        
# 15. Uso dos Módulos os, time, datetime e calendar
# Crie um programa que:
# • Exibe o diretório atual usando os.getcwd().
# • Exibe a data e a hora atuais usando datetime.datetime.now().
# • Exibe o calendário do mês atual usando calendar.month().
# • Faz uma pausa de 3 segundos usando time.sleep(3).

import os
import time
import datetime
import calendar

print(f"Diretório atual: {os.getcwd()}")

print(f"Data e hora atuais: {datetime.datetime.now()}")

print(calendar.month(datetime.datetime.now().year, datetime.datetime.now().month))
