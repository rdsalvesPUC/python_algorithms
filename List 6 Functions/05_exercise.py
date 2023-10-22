# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas

import os
os.system("cls")

# deve retornar o valor final do item, custo + imposto
def somaImposto(taxaImposto, custo):
  custoFinal = ((taxaImposto / 100) * custo) + custo
  return taxaImposto, custoFinal

# entrada de dados
custo = float(input("Custo do produto: "))
taxaImposto = float(input("Taxa: "))

# execução da function somaImposto, retornando um valor para tupla valorFinal
valorFinal = somaImposto(taxaImposto, custo)

print(f"Taxa: {valorFinal[0]}% - Valor Final: {valorFinal[1]}")