# !pip install truth-table-generator

# Bibliotecas
import os
import re
# import ttg
# import pandas as pd

os.system('cls')

# Listas comparativas
# oprCanon = ['^', '∧', '&', 'v', '∨', '~', '¬', '(', ')']
oprNotCanon = ['-', '>', '<', '→', '↔']
oprCanon = {'AND':['^', '∧', '&'],
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
		if i in oprNotCanon:
			errors.append(i)
      
	if errors == []:
		return True
	else:
		return errors
    
# Valida se de fato é uma formula ou somente letras
def isFormula(formula):
	for i in formula:
		if i in oprCanon['AND'] or i in oprCanon['OR']:
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
				return True, '+++ Formula canonica, vamos seguir! +++'

			elif isFormula_result is False:
				return False, '--- Os valores inseridos não possuem operadores. Utilize operadores canônicos e proposições.'

		elif isCanonical_result != []:
			return False, f'--- A formula descrita não é canonica, não utilize o(s) operadore(s): ' + ', '.join(isCanonical_result)
  
	elif haveNumbers_result is True:
		return False, '--- Não utilize números, somente preposições com letras de A-Z'

def validateVector(formula):
	formVector = list(formula)
	formKeys = {}

	# index 0 = pode receber (NOT) ou (PROP1)
	if formVector[0].isalpha():
		formKeys['prop-1'] = formVector[0]

	elif formVector[0] in oprCanon['NOT']:
		formKeys['not-1'] = formVector[0]

	else:
		formKeys['invalid-0'] = formVector[0]

	# index 1 = pode receber (PROP1) ou (OPR1)
	if formVector[0] in oprCanon['NOT']:
		if formVector[1].isalpha():
			formKeys['prop-1'] = formVector[1]
		else:
			formKeys['invalid-1'] = formVector[1]

	elif formVector[0].isalpha():
		if formVector[1] in oprCanon['AND']:
			formKeys['and-1'] = formVector[1]
		elif formVector[1] in oprCanon['OR']:
			formKeys['or-1'] = formVector[1]
		else:
			formKeys['invalid-1'] = formVector[1]

	# index 2 = pode receber (PROP2) ou (OPR1) ou (NOT)
	if formVector[1] in oprCanon['AND'] or formVector[1] in oprCanon['OR']:
		if formVector[2].isalpha():
			formKeys['prop-2'] = formVector[2]
		elif formVector[2] in oprCanon['NOT']:
			formKeys['not-1'] = formVector[2]
		else:
			formKeys['invalid-2'] = formVector[2]

	elif formVector[1].isalpha():
		if formVector[2] in oprCanon['AND']:
			formKeys['and-1'] = formVector[2]
		elif formVector[2] in oprCanon['OR']:
			formKeys['or-1'] = formVector[2]
		else:
			formKeys['invalid-2'] = formVector[2]


	# index 3 = pode receber (PROP2) ou (NOT) ou (OPR2)
	if formVector[2] in oprCanon['AND'] or formVector[2] in oprCanon['OR']:
		if formVector[3].isalpha():
			formKeys['prop-2'] = formVector[3]
		elif formVector[3] in oprCanon['NOT']:
			formKeys['not-2'] = formVector[3]
		else:
			formKeys['invalid-3'] = formVector[3]

	elif formVector[2].isalpha():
		if formVector[3] in oprCanon['AND']:
			formKeys['and-2'] = formVector[3]
		elif formVector[3] in oprCanon['OR']:
			formKeys['or-2'] = formVector[3]
		else:
			formKeys['invalid-3'] = formVector[3]

	# index 4 = pode receber (PROP2) ou (PROP3) ou (OPR2) ou (NOT)
	if formVector[3] in oprCanon['NOT']:
		if formVector[4].isalpha():
			formKeys['prop-2'] = formVector[4]
		else:
			formKeys['invalid-4'] = formVector[4]

	elif formVector[3] in oprCanon['AND'] or formVector[3] in oprCanon['OR']:
		if formVector[4].isalpha():
			formKeys['prop-3'] = formVector[4]
		elif formVector[4] in oprCanon['NOT']:
			formKeys['not-1'] = formVector[4]
		else:
			formKeys['invalid-4'] = formVector[4]
	
	elif formVector[3].isalpha():
		if formVector[4] in oprCanon['AND']:
			if formVector[2] in oprCanon['AND']:
				formKeys['and-2'] = formVector[4]
			else:
				formKeys['and-1'] = formVector[4]

		elif formVector[4] in oprCanon['OR']:
			if formVector[2] in oprCanon['OR']:
				formKeys['or-2'] = formVector[4]
			else:
				formKeys['or-1'] = formVector[4]
		else:
			formKeys['invalid-4'] = formVector[4]

	# index 5 = pode receber (PROP3) ou (OPR2) ou (NOT)
	if formVector[4] in oprCanon['AND'] or formVector[4] in oprCanon['OR']:
		if formVector[5].isalpha():
			formKeys['prop-3'] = formVector[5]
		elif formVector[5] in oprCanon['NOT']:
			formKeys['not-2'] = formVector[5]
		else:
			formKeys['invalid-5'] = formVector[5]

	elif formVector[4] in oprCanon['NOT']:
		if formVector[5].isalpha():
			formKeys['prop-3'] = formVector[5]
		else:
			formKeys['invalid-5'] = formVector[5]

	elif formVector[4].isalpha():
		if formVector[5] in oprCanon['AND']:
			if formVector[2] in oprCanon['AND']:
				formKeys['and-2'] = formVector[5]
			else:
				formKeys['and-1'] = formVector[5]

		elif formVector[5] in oprCanon['OR']:
			if formVector[2] in oprCanon['OR']:
				formKeys['or-2'] = formVector[5]
			else:
				formKeys['or-1'] = formVector[5]
		else:
			formKeys['invalid-5'] = formVector[5]

	# index 6 = pode receber (PROP3) ou (NOT)
	if formVector[5] in oprCanon['AND'] or formVector[4] in oprCanon['OR']:
		if formVector[6].isalpha():
			formKeys['prop-3'] = formVector[6]
		elif formVector[6] in oprCanon['NOT']:
			formKeys['not-3'] = formVector[6]
		else:
			formKeys['invalid-6'] = formVector[6]

	elif formVector[5] in oprCanon['NOT']:
		if formVector[6].isalpha():
			formKeys['prop-3'] = formVector[6]
		else:
			formKeys['invalid-6'] = formVector[6]

	# index 7 = só pode receber (PROP3)
	if formVector[6] in oprCanon['NOT']:
		if formVector[7].isalpha() and formVector[7] not in oprCanon['OR']:
			formKeys['prop-3'] = formVector[7]
		else:
			formKeys['invalid-7'] = formVector[7]

	return formKeys

# input da string pelo usuário
print('### Calculadora de Tabela Verdade ###'.upper())
print('=' * 70)
print('- (Esse aplicativo tem o limite de até 3 proposições: P, Q, R)')
print('- (Crie sua formula em FBF utilizando somente operadores canonicos: ^, v, ~)')
print('- (Não utilize parênteses.)')

while True:
	formula = input('\nDigite sua formula: ')       # recebe a string
	formula = formula.lower()                     # converte para lower case
	formula = formula.replace(' ', '')            # remove possíveis espaços vazios
	formula = formula.replace('(', '').replace(')', '')   # remove todos os brackets

	if fullCheck(formula)[0] is True:
		print(fullCheck(formula)[1])
		
		print(f'\n### Agora vamos validar FBF ###')

		print(validateVector(formula))

	elif fullCheck(formula)[0] is False:
		print(fullCheck(formula)[1])

	choice = input('=== Deseja inserir outra fórmula? (Digite "s" para sim, ou qualquer outra tecla para encerrar): ')
	if choice.lower() != 's':
		break

	







