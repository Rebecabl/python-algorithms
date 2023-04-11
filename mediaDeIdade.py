# Solicite a idade de um grupo de 10 pessoas. Calcule a média de idade do grupo e informe quantas pessoas têm idade acima e abaixo da média.

idades = [0] * 10
soma = 0
for i in range(10):
  idades[i] = int(input('Digite a idade: '))
  soma = soma + idades[i]
media = soma / 10

acima = 0
abaixo = 0
for i in range(10):
  if idades[i] > media:
    acima = acima + 1
  elif idades[i] < media:
    abaixo = abaixo + 1
print(acima,'acima da média e',abaixo,'abaixo da média.')