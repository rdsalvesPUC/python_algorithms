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


# PRIMEIRA PARTE =================================================

# Temos 3 validações cruciais.
# Se a formula não passar por esses 3 pontos, não existe motivo
# para validar se a formula está bem formulada na FBF

# Passar pelas 3 validações básicas
  # Tem números?
  # Tem operadores não canonicos?
  # Tem os operadores AND ou OR? Ou são somente PROPs?
# ================================================================

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


# ENCAPSULAR PARTE UM ==================================================

# Para tornarmos o código simples no momento de evocar as funções,
# estou encapsulando todas as evocações em uma única função chamada fullCheck.
# Com isso, temos o output de toda a primeira parte de uma só vez
# ================================================================

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



# SEGUNDA PARTE ==================================================

# Se passar pelas 3 validações básicas, agora podemos validar se de fato
# a formula está escrita em FBF.

  # Splitar em uma lista
  # Checar qual cumprimento da lista
  # Aplicar as regras de cada posição de 0 a 7
    # Se o valor da posição atende as regras:
      # Definir o que o valor é
      # Salvar o valor em um Dicionario, nomeando a chave e atribuindo o valor
# ================================================================

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

	# Checando o comprimento da formula
	if len(formula) >= 4:

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

		# Checando o comprimento da formula
		if len(formula) >= 5:

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

			# Checando o comprimento da formula
			if len(formula) >= 6:

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

				# Checando o comprimento da formula
				if len(formula) >= 7:

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

					# Checando o comprimento da formula
					if len(formula) == 8:

						# index 7 = só pode receber (PROP3)
						if formVector[6] in oprCanon['NOT']:
							if formVector[7].isalpha() and formVector[7] not in oprCanon['OR']:
								formKeys['prop-3'] = formVector[7]
							else:
								formKeys['invalid-7'] = formVector[7]

	# Depois te checarmos cada posição da formula,
	# e atribuirmos os valores corretos ou o valor INVALID,
	# agora sim, podemos dar o retorno final da função que valida a FBF.
	# Se não há nenhum valor INVALID, então teremos um TRUE para FBF e poderemos continuar
	for key in formKeys.keys():
		if 'invalid' in key:
			return False, '--- Formula não está na FBF, por favor reformule, garantindo que as proposições e operadores estão em uma sequência lógica! ---'

	return True, '+++ Formula está na FBF, vamos seguir! +++', formKeys



# TERCEIRA PARTE ======================================

# Agora que temos certeza de que a formula está bem formulada,
# podemos começar a atribuir os valores bases para as proposições.

# Para isso, varremos o dicionario formKeys através das chaves
# que começam com a string 'prop-'.

# Vamos criar um novo dicionário par armazenar os valores bases das proposições
# ======================================================

def generatePropValues(formKeys):
	basePropValues = {}

	for key, value in formKeys.items():
		if key.startswith('prop-'):
			prop_num = int(key.split('-')[1])
			if prop_num == 1:
				basePropValues[value] = ['V', 'V', 'V', 'V', 'F', 'F', 'F', 'F']
			elif prop_num == 2:
				basePropValues[value] = ['V', 'V', 'F', 'F', 'V', 'V', 'F', 'F']
			elif prop_num == 3:
				basePropValues[value] = ['V', 'F', 'V', 'F', 'V', 'F', 'V', 'F']

	return basePropValues

# QUARTA PARTE ======================================

# Precisamos checar do dicionário formKeys, se existem chaves
# com nome 'not-'.

# Se existirem, isso quer dizer que alguma preposição está sendo negada,
# então seus valores base, precisam ser invertidos.

# Para isso, vamos criar o dicionário NOTbaseProValues para receber as
# proposições que vamos inverter, e atribuir seu respectivos valores.
# ======================================================

def invertPropValues(formKeys):
  # Primeiro vamos validar se existem chaves NOT no dicionário formKeys
	# criamos um novo dicionário para receber esses valores
	notPropValues = {}

	for key in formKeys.keys():
		if 'not-' in key:

			for key, value in formKeys.items():
				if key.startswith('not-'):
					not_num = int(key.split('-')[1])
					prop_key = f'prop-{not_num}'
					if not_num == 1:
						notPropValues[formKeys[key] + formKeys[prop_key]] = ['F', 'F', 'F', 'F', 'V', 'V', 'V', 'V']
					if not_num == 2:
						notPropValues[formKeys[key] + formKeys[prop_key]] = ['F', 'F', 'V', 'V', 'F', 'F', 'V', 'V']
					if not_num == 3:
						notPropValues[formKeys[key] + formKeys[prop_key]] = ['F', 'V', 'F', 'V', 'F', 'V', 'F', 'V']

	return notPropValues


# SÉTIMA PARTE ======================================

# Finalizamos encadeando a execução do código chamando todas as funções
# que foram elaboradas a cima.
# ======================================================


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
		if validateVector(formula)[0] is True:
			print(validateVector(formula)[1])

			print(f'\nFORMULA FORNECIDA PELO USUÁRIO ' + '=' * 25)
			print(formula)

			print(f'\nTABELA VERDADE ' + '=' * 41)

			# Obtendo as chaves e os valores do dicionário
			# generatePropValues_result = generatePropValues(validateVector(formula)[2]).keys()

			if invertPropValues(validateVector(formula)[2]).keys() != {}:
				propositions = list(generatePropValues(validateVector(formula)[2]).keys()) + list(invertPropValues(validateVector(formula)[2]).keys())
				values = list(generatePropValues(validateVector(formula)[2]).values()) + list(invertPropValues(validateVector(formula)[2]).values())

			elif invertPropValues(validateVector(formula)[2]).keys() == {}:
				propositions = list(generatePropValues(validateVector(formula)[2]).keys())
				values = list(generatePropValues(validateVector(formula)[2]).values())

			# Exibindo cabeçalhos
			header = '\t'.join(propositions)
			print(header + '\t')
			print(f'-' * len(header) * 4)

			# Exibindo valores em formato de coluna
			for i in range(len(values[0])):
				row = '\t'.join([values[j][i] for j in range(len(propositions))])
				print(row)

		elif validateVector(formula)[0] is False:
			print(validateVector(formula)[1])

	elif fullCheck(formula)[0] is False:
		print(fullCheck(formula)[1])

	choice = input('\n=== Deseja inserir outra fórmula? (Digite "s" para sim, ou qualquer outra tecla para encerrar): ')
	if choice.lower() != 's':
		break