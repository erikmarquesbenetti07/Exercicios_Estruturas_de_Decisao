'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja
realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
o par ou ímpar;
o positivo ou negativo;
o inteiro ou decimal.'''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Escolha uma operação (+ para adição, - para subtração, * para multiplicação, / para divisão): ")


if operacao == '+':
    resultado = num1 + num2
    operacao_descricao = "adição"
elif operacao == '-':
    resultado = num1 - num2
    operacao_descricao = "subtração"
elif operacao == '*':
    resultado = num1 * num2
    operacao_descricao = "multiplicação"
elif operacao == '/':
    resultado = num1 / num2
    operacao_descricao = "divisão"
else:
    print("Operação inválida")
    resultado = None

par_ou_impar = "par" if resultado % 2 == 0 else "ímpar"

positivo_ou_negativo = "positivo" if resultado >= 0 else "negativo"

inteiro_ou_decimal = "inteiro" if resultado == int(resultado) else "decimal"

if resultado is not None:
    print(f"Resultado da {operacao_descricao}: {resultado}")
    print(f"O número resultante é {par_ou_impar}, {positivo_ou_negativo} e {inteiro_ou_decimal}.")
