# Quadrado mágico.
# Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma.

# Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
    # o 8 3 4
    # o 1 5 9
    # o 6 7 2
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
# Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
# Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3

import os
os.system("cls")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
combinacoes = []

for n in range(1,10):
    for i in lista:
        for j in lista:            
            if n + i + j == 15 and (n != i and n != j and i != j):
                combinacoes.append((n, i, j))


print(combinacoes)