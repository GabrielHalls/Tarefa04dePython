# Curso básico de Python
# Nome do desenvolvedor: Gabriel Vinicius
# Versão 1.0
# Exercicicos de logica de programação
# com logica de programação em python
# 4) Escreva um programa que peça ao usuário para digitar três números e retorne o maior deles.

print("Bom dia, com quem estou interagindo \n")
print("Vamos fazer entrada com três numeros e descobrir qual é o maior deles")

nome = input("Digite seu nome: \n")

def maior_numero():
    # Pedir ao usuário para digitar três números
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    
    # Verificar qual número é o maior
    if num1 >= num2 and num1 >= num3:
        maior = num1
    elif num2 >= num1 and num2 >= num3:
        maior = num2
    else:
        maior = num3
    
    # Retornar o maior número
    return maior

# Chamar a função e imprimir o resultado
print("O maior número é:", maior_numero())