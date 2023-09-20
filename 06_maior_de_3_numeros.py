# Faça um Programa que leia três números e mostre o maior deles

#Solicita ao usuário que insira três números
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))

# Inicializa a varíavel 'maior' com o primeiro número
maior = numero1

# Verifica qual dos números é o maior
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3

# Imprime o maior núemro
print(f'O maior número é: {maior}')