# 1-Faça um programa que imprima na tela os valores entre 20 e 40.

for i in range(20, 41):
    print(i)


# 2-Faça um programa que imprima na tela os valores pares entre 20 e 40.

for i in range(20, 41):
    if i % 2 == 0:
        print(i)


# 3-Faça um programa que imprima os múltiplos de 5 entre 20 e 100.

for i in range(20, 101):
    if i % 5 == 0:
        print(i)

# 4-Faça um programa que imprima os números de 40 a 20 em ordem decrescente.

for i in range(40, 19, -1):
    print(i)             


# 5 - Faça um programa que solicite ao usuário um valor entre 1 e 10. Imprima a tabuada desse número.

numero = int(input("Digite um valor entre 1 e 10: "))

if numero < 1 or numero > 10:
    print("Valor inválido. Por favor, digite um valor entre 1 e 10.")
else:
    print("Tabuada do", numero)
    for i in range(1, 11):
        print(numero, "x", i, "=", numero*i)


    

