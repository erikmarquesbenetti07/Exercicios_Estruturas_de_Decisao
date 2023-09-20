# Faça um Programa que peça dois números e imprima o maior deles


# Solicita ao usuário que insira dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Verifica qual número é o maior
if numero1 > numero2:
    maior = numero1
else:
    maior = numero2

# Imprime o maior número
print(f"O maior número é: {maior}")