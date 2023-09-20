"""Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou VVespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
"Valor Inválido!", conforme o caso."""

turno = input('Em que turno você estuda? (M para matutino, V para vespertino, N para noturno): ')
turno = turno.lower()

if turno == 'm':
    print('Bom dia!')
elif turno == 'v':
    print('Boa Tarde!')
elif turno == 'n':
    print('Boa noite!')
else:
    print('Valor Inválido!')