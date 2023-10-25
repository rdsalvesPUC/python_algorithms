# Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados

import random
import os
os.system("cls")

def embaralhar(texto):
    lista_embaralhada = random.sample(texto, len(texto))
    texto_embaralhado = ''.join(lista_embaralhada)
    
    return texto_embaralhado



texto = str(input("Digite o texto: "))

print(embaralhar(texto))