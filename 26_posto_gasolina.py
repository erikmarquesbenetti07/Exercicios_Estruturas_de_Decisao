'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
o Álcool:
o até 20 litros, desconto de 3% por litro
o acima de 20 litros, desconto de 5% por litro
o Gasolina:
o até 20 litros, desconto de 4% por litro
o acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de
litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da
gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''

preco_gasolina = 2.50
preco_alcool = 1.90

litros_vendidos = float(input("Digite a quantidade de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

if tipo_combustivel == 'A':
    if litros_vendidos <= 20:
        desconto = litros_vendidos * 0.03
    else:
        desconto = litros_vendidos * 0.05
    valor_a_pagar = litros_vendidos * preco_alcool - desconto
elif tipo_combustivel == 'G':
    if litros_vendidos <= 20:
        desconto = litros_vendidos * 0.04
    else:
        desconto = litros_vendidos * 0.06
    valor_a_pagar = litros_vendidos * preco_gasolina - desconto
else:
    print("Tipo de combustível inválido. Use A para álcool ou G para gasolina.")
    valor_a_pagar = 0

if valor_a_pagar > 0:
    print(f"Valor a ser pago: R$ {valor_a_pagar:.2f}")
