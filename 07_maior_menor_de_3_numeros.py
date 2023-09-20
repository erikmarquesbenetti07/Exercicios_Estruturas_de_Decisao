# Faça um Programa que leia três números e mostre o maior e o menor deles

# Solicit ao usuário que insira três números
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo núemro: '))
numero3 = float(input('Digite o terceiro número: '))

# Incializa as variáveis 'maior' e 'menor' com o primeiro número
maior = menor = numero1

# Verifica qual dos números é o maior e o menor
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3

if numero2 < menor:
    menor = numero2
if numero3 < menor:
    menor = numero3

# Imprime o maior e o menor número
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')