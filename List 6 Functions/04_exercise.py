# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo

import os
os.system('cls')

# função para avaliar se um valor é positivo ou negativo
def PositiveOrNegative(n):
    if n > 0:
        return 'P'
    else:
        return 'N'
    
# entrada de dados
n = int(input("Write an integer number: "))

# imprimta o resultado
print(PositiveOrNegative(n))