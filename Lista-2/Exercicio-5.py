# 5. Verificação de Triângulo
# Peça ao usuário três números representando os lados de um triângulo. O programa deve
# verificar e informar se os valores formam um triângulo válido (a soma de dois lados deve ser
# sempre maior que o terceiro).

a = float(input("Digite o 1º lado: "))
b = float(input("Digite o 2º lado: "))
c = float(input("Digite o 3º lado: "))

if a + b > c and a + c > b and b + c > a:
  print("Os lados formam um triângulo válido.")
else:
  print("Os lados não formam um triângulo válido.")
