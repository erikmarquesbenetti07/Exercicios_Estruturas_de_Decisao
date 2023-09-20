'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma
data válida.'''

data = input('Digite uma data no formato dd/mm/aaaa: ')

dia, mes, ano = map(int, data.split('/'))

dias_por_mes = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    dias_por_mes[2] = 29

data_valida = (mes in dias_por_mes) and (1 <= dia <= dias_por_mes[mes])

ano_valido = ano > 0

if data_valida and ano_valido:
    print('A data é válida.')
else:
    print('A data não é válida.')