"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que
deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa
deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
o Desconto do IR:
o Salário Bruto até 900 (inclusive) - isento
o Salário Bruto até 1500 (inclusive) - desconto de 5%
o Salário Bruto até 2500 (inclusive) - desconto de 10%
o Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de
hora é 220."""

valor_hora = float(input('Digite o valor da hora de trabalho: '))
horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas no mês: '))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    desconto_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    desconto_ir = salario_bruto * 0.1
else:
    desconto_ir = salario_bruto * 0.2

desconto_inss = salario_bruto * 0.1

desconto_sindicato = salario_bruto * 0.03

fgts = salario_bruto * 0.11

total_descontos = desconto_ir + desconto_inss + desconto_sindicato

print(f'Salário Bruto: R$ {salario_bruto:.2f}')
print(f'(-) IR (Imposto de Renda): R$ {desconto_ir:.2f}')
print(f'(-) INSS: R$ {desconto_inss:.2f}')
print(f'(-) Sindicato: R$ {desconto_sindicato:.2f}')
print(f'FGTS: R$ {fgts:.2f}')
print(f'Total de descontos: R$ {total_descontos:.2f}')
print(f'Salário Líquido: R$ {salario_bruto:.2f}')