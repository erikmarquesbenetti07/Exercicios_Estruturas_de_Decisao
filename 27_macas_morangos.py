'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
o Até 5 Kg Acima de 5 Kg
o Morango R$ 2,50 por Kg R$ 2,20 por Kg
o Maçã R$ 1,80 por Kg R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$
25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para
ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e
escreva o valor a ser pago pelo cliente.'''

quantidade_morangos = float(input('Digite a quantidade de morangos (em Kg): '))
quantidade_macas = float(input('Digite a quantidade de maçãs (em Kg): '))

preco_morango_ate_5kg = 2.50
preco_morango_acima_5kg = 2.20
preco_maca_ate_5kg = 1.80
preco_maca_acima_5kg = 1.50

if quantidade_morangos <= 5:
    valor_morangos = quantidade_morangos * preco_morango_ate_5kg
else:
    valor_morangos = quantidade_morangos * preco_morango_acima_5kg


if quantidade_macas <= 5:
    valor_macas = quantidade_macas * preco_maca_ate_5kg
else:
    valor_macas = quantidade_macas * preco_maca_acima_5kg


valor_total = valor_morangos + valor_macas


if quantidade_morangos + quantidade_macas > 8 or valor_total > 25.00:
    desconto = 0.10 * valor_total
    valor_total -= desconto

# Imprimir o valor a ser pago pelo cliente
print(f"Valor a ser pago pelo cliente: R$ {valor_total:.2f}")