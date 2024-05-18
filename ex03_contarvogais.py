
# Curso básico de Python
# Nome do desenvolvedor: Gabriel Vinicius
# Versão 1.0
# Exercicicos de logica de programação
# com logica de programação em python
# 3) Escreva um programa que peça ao usuário para digitar uma frase e conte quantas vogais (a, e, i, o, u) ela possui.


frase = input("Digite uma frase: ")

# Inicializa o contador de vogais
contarVogal = 0

# Percorre cada caractere da frase
for caractere in frase:
    # Verifica se o caractere é uma vogal (minúscula)
    if caractere.lower() in 'aeiou':
        # Se for uma vogal, incrementa o contador de vogais
        contarVogal += 1

# Exibe o total de vogais encontradas na frase
print("A frase possui", contarVogal, "vogais.")

