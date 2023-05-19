import random
import time
Palavras = "cocada", "cuscuz", "galeto", "pastel"
Chances = 6
Jogador = []
Palavras = random.choice(Palavras)
Ganhou = False

print("="*20)
print("Jogo da Forca\n"
   "Bem-vindo")
print("="*20)
print("Vamos começar o jogo?")

Jogar = input("SIM ou NÂO\n")

if Jogar == "SIM":
    print("Tente adivinhar palavras relacionadas à Comida!")
    print(f"Você tem {Chances} chances para acertar a palavra.")
    print("\033[31mPensando em palavra....")
    time.sleep(3)
    print("\033[33mPalavra escolhida com sucesso!")
    while True:
        for letras in Palavras:
            if letras in Jogador:
                print(letras, end=" ")
            else:
                print("_", end=" ")
        print(" \n")
        print(f"\033[31mVocê tem {Chances} chances!")
        Tentativas = input("\033[33mEscolha uma letra ")
        Jogador.append(Tentativas)

        Ganhou = True

        for letra in Palavras:
            if letra not in Jogador:
                Ganhou = False

        if Chances == 1 or Ganhou:
            break

        if Tentativas not in Palavras:
            Chances -= 1

    if Ganhou:
        time.sleep(2)
        print(f"Parabéns, você ganhou a palara era {Palavras}.")
    else:
        time.sleep(2)
        print(f"Você perdeu o jogo, a palara era {Palavras}.")

else:
    print("Até a próxima!")
    Ganhou = True


