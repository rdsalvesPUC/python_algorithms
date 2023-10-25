# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado

import os
os.system("cls")

def digi_counter(numero):
    counter = 0
    for i in str(numero):
        counter += 1
    return counter

numero = int(input("Digite um número inteiro: "))
print(digi_counter(numero))