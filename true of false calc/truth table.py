# Bibliotecas
import os
import re

os.system('cls')


# Listas comparativas
operadoresCanonicos = ['^', '∧', '&', 'v', '∨', '~', '¬', '(', ')']
operadoresNaoCanonicos = ['-', '>', '<', '→', '↔']

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

# # Splita dados, armazenas em cada lista e valida se a formula é canonica
# def isCanonical(formula):
#     # Listas vazias para receber os valores após o split da string
#     operadores = []
#     proposicoes = []
#     errors = []

#     # split de dados em cada lista
#     for i in formula:
#         if i in operadoresCanonicos:
#             operadores.append(i)
#         elif i in operadoresNaoCanonicos:
#             errors.append(i)
#         elif i not in operadoresCanonicos and i not in operadoresNaoCanonicos:
#             proposicoes.append(i)
    
#     if errors != []:
#         return False
    
#     return operadores, proposicoes





# input da string pelo usuário
print(f'### Calculadora de Tabela Verdade ###')
print(f'(Crie sua formula em FBF utilizando somente operadores canonicos: ^, v, ~)\n')

while True:
    formula = input('Digite sua formula: ')       # recebe a string
    formula = formula.lower()                     # converte para lower case
    formula = formula.replace(' ', '')            # remove possíveis espaços vazios

    # Recebe o resultado da função haveNumbers
    haveNumbers_result = haveNumbers(formula)         
    
    # Se não tem números, validamos se tem operadores errados
    if haveNumbers_result ==  False:
        isCanonical_result = isCanonical(formula)       # Recebe o resultado da função isCanonical
        if isCanonical_result == True:
            print('--Formula canonica, vamos seguir!\n')
            break
        elif isCanonical_result != []:
            print(f'--A formula descrita não é canonica, não utilize o(s) operadore(s): ' + ', '.join(isCanonical_result) + '\n')
    
    elif haveNumbers_result == True:
        print(f'--Não utilize números, somente preposições com letras de A-Z\n')
    

print(f'\n### Agora vamos validar FBF ###')

# Agora vamos validar a FBF

# # validar se a string está na fbf (forma canonica, somente: ^ v ~)
# for i in formula:
#   if i in operadoresNaoCanonicos:
#     print('A formula descrita não esta na Norma de FBF, digite novamente.')



    # True, imprime a tabela verdade

    # False, retorna erro, avisa que não está bem formulada

      # Solicita uma nova entrada de dadosa

      # Se digitar 0, encerra o programa

# # Output
# print(f'Formula: {input}')
# print(f'Resultado')
# print(f'{prop1}{prop2}{prop3}')

# # Exemplo de output
# Formula:
# p	q	r	(~p)	(~q)	((~p)^(~q))	(~r)	(((~p)^(~q))v(~r))
# F	F	F	  V	    V	       V	      V             	V
# F	F	V	  V	    V	       V	      F             	V
# F	V	F	  V	    F	       F	      V             	V
# F	V	V	  V	    F	       F	      F             	F
# V	F	F	  F	    V	       F	      V             	V
# V	F	V	  F	    V	       F	      F             	F
# V	V	F	  F	    F	       F	      V             	V
# V	V	V	  F	    F	       F	      F             	F