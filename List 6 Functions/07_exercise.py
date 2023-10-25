# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso

import os
os.system("cls")

def valorPagamento(prestacao, dias_atraso):
    if dias_atraso == 0:
        return prestacao # Para pagamentos sem atraso, cobrar o valor da prestação.

    else:
        multa = prestacao * 0.03 # Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso
        juros = prestacao * (0.001 * dias_atraso)
        prestacao_total = prestacao + multa + juros
        return prestacao_total

prestacoesCounter = 0
prestacoesSoma = 0

while True:
    prestacao = float(input("Informa o valor da prestação: "))
    if prestacao == 0:
        break

    dias_atraso = int(input("Quantos dias está atrasada: "))
    resultado = valorPagamento(prestacao, dias_atraso)
    print(f"\nPrestação nº {prestacoesCounter + 1} ficou em: R$ {resultado}\n")

    prestacoesCounter += 1
    prestacoesSoma += resultado

print(f"\nRelatório do dia:\n"
      f"Quantidade de prestações pagas: {prestacoesCounter}\n"
      f"Valor total das prestações pagas: R${prestacoesSoma:.2f}")