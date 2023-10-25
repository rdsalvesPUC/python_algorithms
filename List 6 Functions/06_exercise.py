# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

import os
os.system("cls")

# Func de converção
def conversao(horas):
  if horas == 12:
    horas_convertidas = horas
    am_pm = "P"
  elif horas > 12:
    horas_convertidas = horas - 12 # Só precisamos converter após meio dia, 13h - 12 = 1h e etc...
    am_pm = "P"
  else:
    horas_convertidas = horas # Se for menor que 12, então ainda estamos no periodo da manha e não precisamos converter
    am_pm = "A"
  return horas_convertidas, am_pm

# Func saida dos dados
def saida_horas():
  horas12 = conversao(horas)
  return f"{horas12[0]}:{minutos} {horas12[1]}"

# Entrada de dados
while True:
  horas = int(input("Digite as horas em formato 24h: ")) # Digite horas em números inteiros
  minutos = int(input("Digite os minutos: ")) # Digite minutos em números inteiros
  print(saida_horas())

  encerrar = input(f"\nDeseja encerrar o programa, digite S: \n").upper()
  if encerrar == 'S':
    break