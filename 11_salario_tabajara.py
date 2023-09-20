"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
contraram para desenvolver o programa que calculará os reajustes.
o Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:
o salários até R$ 280,00 (incluindo) : aumento de 20%
o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
o salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
informe na tela:
o o salário antes do reajuste;
o o percentual de aumento aplicado;
o o valor do aumento;
o o novo salário, após o aumento."""

salario_atual = float(input('Digite o salário atual do colaborador: '))

percentual_aumento = 0
valor_aumento = 0

if salario_atual <= 280.00:
    percentual_aumento = 20
elif salario_atual <= 700.00:
    percentual_aumento = 15
elif salario_atual <= 1500.00:
    percentual_aumento = 10
else:
    percentual_aumento = 5

valor_aumento = (percentual_aumento / 100) * salario_atual
novo_salario = salario_atual + valor_aumento

print(f'Salário antes do reajuste: R$ {salario_atual:.2f}')
print(f'Percentual do aumento aplicado: {percentual_aumento}%')
print(f'Valor do aumento: R$ {valor_aumento:.2f}')
print(f'Novo salário após o aumento: R$ {novo_salario:.2f}')