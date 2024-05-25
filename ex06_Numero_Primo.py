# Curso básico de Python
# Nome do desenvolvedor: Gabriel Vinicius
# Versão 1.0
# Exercicicos de logica de programação
# com logica de programação em python
# 6) Faça um programa que receba um número inteiro e retorne se é primo ou não.
# exemplo 2,3,5,7,11,13,17,19,23

numero = int(input("Digite um numero inteiro: "))


#if numero <=1 :
#        print("O numero não é primo")
#elif numero% 2 == 0 and numero != 2:
#    print("O numero não é primo")
#elif numero% 3 == 0 and numero != 3 :
#    print("O numero não é primo")
#elif numero% 5 == 0 and numero != 5 :
#        print("O numero não é primo")
#elif numero% 7 == 0 and numero != 7 :
#            print("O numero não é primo")
#elif numero% 11 == 0 and numero != 11 :
#                print("O numero não é primo")
#elif numero% 13 == 0 and numero != 13 :
#                    print("O numero não é primo")
#elif numero% 17 == 0 and numero != 17 :
#                        print("O numero não é primo")
#elif numero% 19 == 0 and numero != 19 :
#                            print("O numero não é primo")
#elif numero% 23 == 0 and numero != 23 :
#                                print("O numero não é primo")
#else:
#        print("O numero é primo")

if numero<=1:

    print("O número não é primo")

elif numero%2==0 and numero!=2:

    print("O número não é primo")

elif numero%3==0 and numero!=3 or numero%5==0 and numero!=5 or numero%7==0 and numero!=7:

  print("O número não é primo")

else:

    print("O número é primo")