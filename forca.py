import random
from typing import List

def jogar():
    apresentacao()
    palavra_secreta = palavras_secretas()

    letras_acertadas = inicializa_letras_certas(palavra_secreta)
    qtd_letra = letras_acertadas.count("_")
    print("Essa palavra tem", qtd_letra, "letras", letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):

        chute= tentativas_adivinhacao()

        if (chute in palavra_secreta):
            adiciona_letra(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            total_tentativas = qtd_letra - erros
            if total_tentativas >= 1:
                mensagem_tantaiva(total_tentativas)

        enforcou = erros == qtd_letra

        acertou ="_" not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        mensagem_ganhador()
    else:
        mensagem_perdedor(palavra_secreta)



def apresentacao():
    print("*******************************")
    print("**Bem vindo ao jogo da Forca!**")
    print("*******************************")

def palavras_secretas():
    with open("palavras.txt") as arquivo:
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_letras_certas(palavra):
    return ["_" for letra in palavra]


def tentativas_adivinhacao():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def adiciona_letra(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def mensagem_tantaiva(total_tentativas):
    print("Opss, você errou uma letra, ainda restam {} tentativas.".format(total_tentativas))

def mensagem_ganhador():
    print("Parabéns, você acertou a palavra secreta!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagem_perdedor(palavra_secreta):
    print("Suas tentativas acabaram, você perdeu!!\n A palavra secreta era: {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if(__name__ == "__main__"):
    jogar()