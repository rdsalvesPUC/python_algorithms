# Desenha moldura.
# Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘.
# Esta função deve receber dois parâmetros, linhas e colunas,
# sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20.
# Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante

import os
os.system("cls")

def desenhar_retangulo(linhas=1, colunas=1):

    # Se os valores forem maiores que 20, ajustamos para 20. Se os valores forem menores que 1, ajustamos para 1
    if linhas > 20: linhas = 20
    elif linhas < 1: linhas = 1

    if colunas > 20: colunas = 20
    elif colunas < 1: colunas = 1


    # Se só temos 1 coluna e 1 linha, então só temos um sinal de '+'
    if colunas == 1 and linhas == 1:
        print(f"+")

    elif colunas == 1 and linhas > 1:
        for i in range(linhas):
            if i == 0:
                print(f"+")
            else:
                print(f"|")

    elif colunas >= 2:
        for i in range(linhas):
            if i == 0 or i == linhas - 1:
                print(f"+" + "-" * (colunas - 2) + "+")
            else:
                print(f"|" + " " * (colunas - 2) + "|")



# Entrada de dados, input de linhas e colunas
linhas = int(input("Digite o número de linhas (1-20): "))
colunas = int(input("Digite o número de colunas (1-20): "))
desenhar_retangulo(linhas, colunas)