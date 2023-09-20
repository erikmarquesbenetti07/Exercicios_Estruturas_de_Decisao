# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

# Solicita ao usuário que insira uma letra
letra = input('Digite uma letra (F para Feminino ou M para Masculino): ')

# Converte a letra para maiúscula para tornar a comparação insensível a maiúsculas/minúsculas
letra = letra.upper()

# Verifica a letra e imprime a mensagem correspondente 
if letra == "F":
    print('Feminino')
elif letra == "M":
    print('Masculino')
else:
    print('Sexo Inválido')