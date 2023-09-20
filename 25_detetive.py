'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
o "Telefonou para a vítima?"
o "Esteve no local do crime?"
o "Mora perto da vítima?"
o "Devia para a vítima?"
o "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino". Caso contrário, ele será classificado como "Inocente".'''

respostas_positivas = 0

pergunta1 = input("Telefonou para a vítima? (s/n): ")
if pergunta1.lower() == 's':
    respostas_positivas += 1

pergunta2 = input("Esteve no local do crime? (s/n): ")
if pergunta2.lower() == 's':
    respostas_positivas += 1

pergunta3 = input("Mora perto da vítima? (s/n): ")
if pergunta3.lower() == 's':
    respostas_positivas += 1

pergunta4 = input("Devia para a vítima? (s/n): ")
if pergunta4.lower() == 's':
    respostas_positivas += 1

pergunta5 = input("Já trabalhou com a vítima? (s/n): ")
if pergunta5.lower() == 's':
    respostas_positivas += 1

if respostas_positivas == 2:
    print("Você é classificado como 'Suspeito'.")
elif 3 <= respostas_positivas <= 4:
    print("Você é classificado como 'Cúmplice'.")
elif respostas_positivas == 5:
    print("Você é classificado como 'Assassino'.")
else:
    print("Você é classificado como 'Inocente'.")
