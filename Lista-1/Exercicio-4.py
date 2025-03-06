# Faça um programa que pergunte o número de horas trabalhadas no mês e o valor recebido
# por hora. O programa deve calcular e exibir o salário total do mês.

hours, minutes = map(int, input("Digite o número de horas trabalhadas no mês no formato HH:MM:").split(':'))
value = float(input("Digite o valor recebido por hora: "))

total_hours = hours + (minutes / 60)
salary = total_hours * value

print(f"O salário total do mês é R${salary:.2f}")