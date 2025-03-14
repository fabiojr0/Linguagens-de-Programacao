# 5. Conversão de Temperatura
# Crie uma função que converta temperaturas de Celsius para Fahrenheit. No
# programa principal, solicite uma temperatura ao usuário em graus Celsius e utilize
# a função para exibir o valor correspondente em Fahrenheit.

def celsius_para_fahrenheit(celsius):
    return celsius * 9/5 + 32

celsius = float(input("Digite a temperatura em graus Celsius: "))

print(f"A temperatura em Fahrenheit é: {celsius_para_fahrenheit(celsius):.2f}")