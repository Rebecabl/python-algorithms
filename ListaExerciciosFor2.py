# 6 - Faça um programa que imprima os números de 1 a 100. Entretanto, os múltiplos de 4 devem ser substituídos pela palavra “PIM”. Saída esperada:
# 1 2 3 PIM 5 6 7 PIM 9 10 11 PIM 13 14

for i in range(1, 101):
    if i % 4 == 0:
        print("PIM", end=" ")
    else:
        print(i, end=" ")

# 7 - Faça um programa que solicite ao usuário um valor entre 1 e 10. Imprima os números de 1 a 100, substituindo os múltiplos do valor fornecido pela palavra “PIM”.
# Ex.: o usuário digita 7
# 1 2 3 4 5 6 PIM 8 9 10 11 12 13 PIM 15 16 17 18 19 20 PIM 22

valor = int(input("Digite um valor entre 1 e 10: "))

if valor < 1 or valor > 10:
    print("Valor inválido. Por favor, digite um valor entre 1 e 10.")
else:
    for i in range(1, 101):
        if i % valor == 0:
            print("PIM", end=" ")
        else:
            print(i, end=" ")


# 8 - Faça um programa que imprima na tela os números entre dois valores fornecidos pelo usuário. Ex.: Usuário informa 7 e 15
# 7 8 9 10 11 12 13 14 15


inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))

for i in range(inicio, fim+1):
    print(i, end=" ")


# 9 - Faça um programa que leia 10 valores informados pelo usuário. Informe quantos valores foram pares e quantos valores foram ímpares.

pares = 0
impares = 0

for i in range(1, 11):
    valor = int(input("Digite o {}º valor: ".format(i)))
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de valores pares: ", pares)
print("Quantidade de valores ímpares: ", impares)


# 10 - Faça um programa que imprima os n primeiros números da sequência de Fibonacci. O valor de n deve ser informado pelo usuário.
# Ex.: Usuário digita 10
# 1 1 2 3 5 8 13 21 34 55


pares = 0
impares = 0

for i in range(1, 11):
    valor = int(input("Digite o {}º valor: ".format(i)))
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de valores pares: ", pares)
print("Quantidade de valores ímpares: ", impares)


