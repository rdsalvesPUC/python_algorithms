# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721

import os
os.system("cls")

def convert_to_list(numero):
    num_expandido = []
    for i in str(numero):
        num_expandido.append(int(i))
    return num_expandido

def reverse():
    lista_reversa = convert_to_list(numero)
    lista_reversa.reverse()

    num_invertido = ""
    # num_invertido = ''.join(lista_reversa)
    for i in lista_reversa:
        num_invertido += str(i)

    return int(num_invertido)


numero = int(input("Digite um número inteiro: "))
print(reverse())