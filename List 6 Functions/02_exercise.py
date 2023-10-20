# Faça um programa para imprimir:
    # o 1
    # o 1 2
    # o 1 2 3
    # o .....
    # o 1 2 3 ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha

import time
import os

os.system('cls')

# função para imprimir as repetições de N
def n_lines(n):
    for i in range (1, n + 1):
        for j in range(1, i + 1):
            print(f"{j} ", end="")
        print()
        time.sleep(0.1)

# receber o valor de N
n = int(input("Write an integer number: "))

# imprima o resultado
n_lines(n)



