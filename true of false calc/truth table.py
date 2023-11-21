# !pip install truth-table-generator

# Bibliotecas
import os
import re
# import ttg
# import pandas as pd

os.system('cls')


# Listas comparativas
# operadoresCanonicos = ['^', '∧', '&', 'v', '∨', '~', '¬', '(', ')']
operadoresNaoCanonicos = ['-', '>', '<', '→', '↔']
operadoresCanonicos = {'AND':['^', '∧', '&'],
                       'OR': ['v', '∨', 'v'],
                       'NOT': ['~', '¬'],
                       'BRACKET': ['(', ')']}

# Valida se existem números na formula
def haveNumbers(formula):
  for i in formula:
    for j in range(10):
      if i == str(j):
        return True
      
  return False

# Valida se a formula é canonica
def isCanonical(formula):
  # Armazena os operadores que não deveriam ser usados
  errors = []

  # Varredura de dados
  for i in formula:
    if i in operadoresNaoCanonicos:
      errors.append(i)
      
  if errors == []:
    return True
  else:
    return errors
    
# Valida se de fato é uma formula ou somente letras
def isFormula(formula):
  for i in formula:
    if i in operadoresCanonicos['AND'] or i in operadoresCanonicos['OR']:
      return True
    
  return False
    
def fullCheck(formula):
  # Confere se não tem números
  haveNumbers_result = haveNumbers(formula)
  if haveNumbers_result is  False:

    # Confere se tem operadores não canonicos
    isCanonical_result = isCanonical(formula)
    if isCanonical_result is True:
      
      # Confere se na formula existe pelo menos um operador canonico ou se são somente letras
      isFormula_result = isFormula(formula)
      if isFormula_result is True:
        return '+++ Formula canonica, vamos seguir! +++'

      elif isFormula_result is False:
         return '--- Os valores inseridos não possuem operadores. Utilize operadores canônicos e proposições.'

    elif isCanonical_result != []:
      return f'---A formula descrita não é canonica, não utilize o(s) operadore(s): ' + ', '.join(isCanonical_result)
  
  elif haveNumbers_result is True:
      return '--- Não utilize números, somente preposições com letras de A-Z'




# input da string pelo usuário
print(f'### Calculadora de Tabela Verdade ###')
print(f'(Crie sua formula em FBF utilizando somente operadores canonicos: ^, v, ~)')

while True:
  formula = input('\nDigite sua formula: ')       # recebe a string
  formula = formula.lower()                     # converte para lower case
  formula = formula.replace(' ', '')            # remove possíveis espaços vazios
  formula = formula.replace('(', '').replace(')', '')   # remove todos os brackets

  print(fullCheck(formula))

  choice = input('=== Deseja inserir outra fórmula? (Digite "s" para sim, ou qualquer outra tecla para encerrar): ')
  if choice.lower() != 's':
      break
    
formulaVector = list(formula)

print(f'\n### Agora vamos validar FBF ###')