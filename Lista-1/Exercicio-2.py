# 2. Conversão de Temperatura
# Faça um programa que leia uma temperatura em graus Celsius e a converta para Fahrenheit.
# A fórmula de conversão é:
# O programa deve exibir o valor convertido.

def convertToFahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = convertToFahrenheit(celsius)
print(f"A temperatura em Fahrenheit é {fahrenheit:.2f}")