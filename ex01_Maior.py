# Curso básico de Python
# Nome do desenvolvedor: Gabriel Vinicius
# Versão 1.0
# Exercicicos de logica de programação
# com logica de programação em python
# 1) Faça um programa que receba a idade do usuário e imprima se ele é maior de idade ou não.



print("Bom dia tudo bem?")
nome = input("Digite seu nome: ")

print("\n")

print(nome + ", você pode me informar sua idade? Assim podemos verificar se você é um adulto ou menor de idade.")

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


