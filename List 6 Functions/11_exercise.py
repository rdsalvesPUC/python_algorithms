# Data com mês por extenso.
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

import os
os.system("cls")

meses = {1:"Janeiro", 2:"Feveiro", 3:"Março", 4:"Abril", 5:"Maio", 6:"Junho",
         7:"Julho", 8:"Agosto", 9:"Setembro", 10:"Outubro", 11:"Novembro", 12:"Dezembro"}

# Construa uma função que receba uma data no formato DD/MM/AAAA
def data_numerica(dia, mes, ano):
  if not (1 <= mes <= 12 and 1 <= dia <= 31):
    return None

  # Convertendo mês númerico para mês por extenso
  mesPorExtenso = meses[mes]

  # Devolva uma string no formato D de mesPorExtenso de AAAA.
  return f"{dia} de {mesPorExtenso} de {ano}"


# Entrada de dados, recebemos a data em formato númerico,
data = input("Digite a data desejada no formato DD/MM/AAAA: ")

# Precisamos separar o que é DIA, MES e ANO em diferentes variaveis para poder tratar cada uma
partes_data = data.split("/")

# Atribuimos os valores a cada variável, ja convertendo de STR >>> INT
dia = int(partes_data[0])
mes = int(partes_data[1])
ano = int(partes_data[2])

print(f"Data convertida para: {data_numerica(dia, mes, ano)}")