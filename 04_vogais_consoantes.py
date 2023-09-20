# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# Solicita ao usuário que insira uma letra
letra = input('Digite uma letra: ')

# Converte a letra para minúscula para facilitar a comparação
letra = letra.lower()

# Verifica se a letra é uma vogal
if letra in 'aeiou':
    print('A letra é uma vogal.')
else:
    print('A letra é uma consoante.')