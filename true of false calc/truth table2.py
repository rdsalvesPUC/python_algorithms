#Paula 1
import os

os.system('clear')

# Listas comparativas
operadoresCanonicos = ['^', '∧', 'v', '∨', '~', '¬', '(', ')']

# Valida se existem números na fórmula
def haveNumbers(formula):
    for i in formula:
        for j in range(10):
            if i == str(j):
                return True
    return False

# Valida se a fórmula é canônica
def isCanonical(formula):
    for i in formula:
        if i not in operadoresCanonicos and not i.isalpha():
            return False
    return True

# Traduz a fórmula para linguagem de programação
def translateFormula(formula):
    translation = formula
    for op in operadoresCanonicos:
        if op == '^':
            translation = translation.replace(op, ' and ')
        elif op == 'v':
            translation = translation.replace(op, ' or ')
        elif op == '~':
            translation = translation.replace(op, ' not ')
    return translation

# Função para imprimir a tabela verdade
def printTruthTable(variables, formula):
    interpretations = generateInterpretations(variables)

    header = '\t'.join(variables + [formula])
    print(header)
    print('-' * (len(header) + 8))

    for interpretation in interpretations:
        values = [interpretation[var] and 'V' or 'F' for var in variables]
        result = evaluateFormula(formula, interpretation) and 'V' or 'F'
        row = '\t'.join(values + [result])
        print(row)

# Função para gerar todas as interpretações possíveis
def generateInterpretations(variables):
    n = len(variables)
    interpretations = []
    for i in range(2**n):
        interpretation = {}
        binary_repr = format(i, f'0{n}b')  # Representação binária com zero à esquerda
        for j in range(n):
            interpretation[variables[j]] = bool(int(binary_repr[j]))
        interpretations.append(interpretation)
    return interpretations


# Função para calcular o valor da fórmula para uma interpretação
def evaluateFormula(formula, interpretation):
    local_vars = interpretation.copy()
    code = compile(formula, '<string>', 'eval')
    return eval(code, None, local_vars)


# input da string pelo usuário
print(f'Calculadora de Tabela Verdade')
print(f'(Crie sua formula em FBF utilizando somente operadores canônicos: ^, v, ~)\n')

while True:
    formula = input('Digite sua formula: ')
    formula = formula.lower().replace(' ', '')

    haveNumbers_result = haveNumbers(formula)

    if haveNumbers_result is False:
        isCanonical_result = isCanonical(formula)
        if isCanonical_result is True:
            print('Formula canônica, vamos seguir!')

            # Traduz a fórmula para linguagem de programação
            translated_formula = translateFormula(formula)

            # Fórmula está correta, imprimir a tabela verdade
            variables = [var for var in set(formula) if var.isalpha() and var.islower()][:3]
            print('Variáveis proposicionais encontradas:', ', '.join(variables))
            print('Tabela Verdade:')
            printTruthTable(variables, translated_formula)
        else:
            print(f'\nA fórmula descrita não é canônica, utilize apenas operadores canônicos e variáveis válidas.')
    elif haveNumbers_result is True:
        print(f'\nNão utilize números, somente proposições com letras de A-Z')

    choice = input('Deseja inserir outra fórmula? (Digite "s" para sim, ou qualquer outra tecla para encerrar): ')
    if choice.lower() != 's':
        break
