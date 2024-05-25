# Curso básico de Python
# Nome do desenvolvedor: Gabriel Vinicius
# Versão 1.0
# Exercicicos de logica de programação
# com logica de programação em python
# 5) Escreva um programa que peça ao usuário para digitar um número e verifique se é positivo, negativo ou zero.

print("Olá tudo bem ? \n")
print("Aqui nesse exercicios vamos descobrir se o numero é positvo ou negativo ou zero")

nome = input("Digite seu nome: \n")

numero = float(input("Digite um numero: \n"))

if numero > 0:
    print("O numero digitado é positivo")
elif numero < 0:
    print("O numero digitado é nagativo")
else:
    print("O numero digitado é zero")
    