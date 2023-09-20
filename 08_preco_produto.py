"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve
comprar, sabendo que a decisão é sempre pelo mais barato"""

# Solicita ao usuário que insira o preço de três produtos
preco_produto1 = float(input('Digite o preço do primeiro produto: '))
preco_produto2 = float(input('Digite o preço do segundo produto: '))
preco_produto3 = float(input('Digite o preço do terceiro produto: '))

# Inicializa a variável 'produto_mais_barato' com o preço do primeiro produto
produto_mais_barato = preco_produto1

# Compara os preços dos produtos para encontrar o mais barato
if preco_produto2 < produto_mais_barato:
    produto_mais_barato = preco_produto2

if preco_produto3 < produto_mais_barato:
    produto_mais_barato = preco_produto3

# Imprime o produto mais barato
if produto_mais_barato == preco_produto1:
    print('Você deve comprar o primeiro produto.')
elif produto_mais_barato == preco_produto2:
    print('Você deve comprar o segundo produto.')
else:
    print('Você deve comprar o terceiro produto.')
