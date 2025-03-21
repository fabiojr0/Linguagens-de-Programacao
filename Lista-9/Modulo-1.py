# Módulo 1 - Módulos, Pacotes e PIP
# 1. Importação de Módulos
# Escreva um programa que importe os módulos math e random e use suas funções para:
# • Calcular a raiz quadrada de um número informado pelo usuário.
# • Gerar um número aleatório entre 1 e 100.

import math
import random

numero = float(input("Digite um número: "))

print(f"A raiz quadrada de {numero} é {math.sqrt(numero)}.")

print(f"Número aleatório entre 1 e 100: {random.randint(1, 100)}.")


# 2. Uso do Módulo platform
# Crie um programa que exiba informações sobre o sistema operacional usando o módulo
# platform. O programa deve imprimir:
# • Nome do sistema operacional
# • Versão do sistema
# • Arquitetura do processador

import platform

print(f"Nome do sistema operacional: {platform.system()}")

print(f"Versão do sistema: {platform.version()}")

print(f"Arquitetura do processador: {platform.architecture()}")


# 3. Criando e Usando um Módulo Personalizado
# Crie um módulo chamado meu_modulo.py contendo uma função dobro(n) que retorna
# o dobro de um número. Depois, escreva um programa principal que importe esse
# módulo e utilize a função.

import meu_modulo

numero = float(input("Digite um número: "))

print(f"O dobro de {numero} é {meu_modulo.dobro(numero)}.")

