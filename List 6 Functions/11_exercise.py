# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

import os
os.system("cls")

def data_numerica(dia, mes, ano):
    return f"{dia} de {mesPorExtenso} de {ano}"

data = input("Digite a data desejada no formato DD/MM/AAAA: ")
