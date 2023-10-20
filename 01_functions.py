# Faça um programa para imprimir:
    # o 1
    # o 2 2
    # o 3 3 3
    # o .....
    # o n n n n n n ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha

import time
import os

os.system('cls')

# função para imprimir as repetições de N
def n_linhas(n):
    for i in range(1, n + 1):
        print(f"{i} " * i)
        time.sleep(0.1)

# receber o valor de N
n = int(input("Digite um número inteiro: "))

# imprimta o resultado
print(n_linhas(n))