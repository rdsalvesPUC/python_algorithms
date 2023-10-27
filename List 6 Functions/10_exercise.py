# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se,

# na primeira jogada, você tirar 7 ou 11, você é um "natural" e ganhou.
# Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".

# Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente

import time
import random
import os
os.system("cls")

def jogar_dados():
    dado = random.randint(2,13)
    return dado

natural = [7, 11]
craps = [2, 3, 12]
ponto = [4, 5, 6, 8, 9, 10]

resultado1 = jogar_dados()

if resultado1 in natural:
    print(resultado1)
    print(f"Você é um 'natural' e ganhou!")

elif resultado1 in craps:
    print(resultado1)
    print(f"CRAPS! Você perdeu")

elif resultado1 in ponto:
    print(f"Você marcou {resultado1} pontos")

    resultado2 = 0

    while resultado2 != resultado1:
        resultado2 = jogar_dados()
        print(f"Seu número foi {resultado2}.")
        time.sleep(0.2)


        if resultado2 == resultado1:
            print(f"Você marcou {resultado2} pontos novamente! Você ganhou")
            break

        elif resultado2 == 7:
            print(f"CRAPS! Você tirou 7 e perdeu")
            break
        
        else:
            continue

