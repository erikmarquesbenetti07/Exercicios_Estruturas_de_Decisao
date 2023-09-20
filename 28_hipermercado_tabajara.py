'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
o Até 5 Kg Acima de 5 Kg
o File Duplo R$ 4,90 por Kg R$ 5,80 por Kg
o Alcatra R$ 5,90 por Kg R$ 6,80 por Kg
o Picanha R$ 6,90 por Kg R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne
da promoção, porém não há limites para a quantidade de carne por cliente. Se compra
for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da
compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade
de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.'''

preco_file_duplo_ate_5kg = 4.90
preco_file_duplo_acima_5kg = 5.80
preco_alcatra_ate_5kg = 5.90
preco_alcatra_acima_5kg = 6.80
preco_picanha_ate_5kg = 6.90
preco_picanha_acima_5kg = 7.80

tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra ou Picanha): ").capitalize()
quantidade_comprada = float(input(f"Digite a quantidade de {tipo_carne} (em Kg): "))

if quantidade_comprada <= 5:
    if tipo_carne == "File Duplo":
        preco_total = quantidade_comprada * preco_file_duplo_ate_5kg
    elif tipo_carne == "Alcatra":
        preco_total = quantidade_comprada * preco_alcatra_ate_5kg
    elif tipo_carne == "Picanha":
        preco_total = quantidade_comprada * preco_picanha_ate_5kg
else:
    if tipo_carne == "File Duplo":
        preco_total = quantidade_comprada * preco_file_duplo_acima_5kg
    elif tipo_carne == "Alcatra":
        preco_total = quantidade_comprada * preco_alcatra_acima_5kg
    elif tipo_carne == "Picanha":
        preco_total = quantidade_comprada * preco_picanha_acima_5kg

pagamento = input("Digite o tipo de pagamento (Dinheiro ou Cartão Tabajara): ").capitalize()
desconto = 0.0

if pagamento == "Cartão Tabajara":
    desconto = 0.05 * preco_total

valor_a_pagar = preco_total - desconto

print("\nCupom Fiscal")
print(f"Tipo de carne: {tipo_carne}")
print(f"Quantidade: {quantidade_comprada} Kg")
print(f"Preço total: R$ {preco_total:.2f}")
print(f"Tipo de pagamento: {pagamento}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
