import random 

print("Bem-vindo ao jogo!!!")

jogador = {
    #HP: Vida
    #DEF: Defesa
    #ATQ: Ataque
    "HP": random.randint(200, 1000), 
    "ATQ": random.randint(1, 50),
    "DEF": random.randint(1, 50)
}
computador = {
    "HP": random.randint(200, 1000),
    "ATQ": random.randint(1, 50),
    "DEF": random.randint(1, 50)
}

while True:
    print("Menu\n")
    print("1-Iniciar jogo\n")
    print("2-Sair\n")
    escolha = input("Escolha uma da opções acima: ")

    if escolha == "2":
        print("Você saiu do jogo.")
        break

    elif escolha == "1":
        print("O Duelo começou...\n")
        print("Você")
        print(f"HP: {jogador['DEF']}")
        print("Inimigo (computador)")
        print(f"HP: {computador['HP']}")
        print(f"Ataque: {computador['ATQ']} DEF: {computador['DEF']}\n")

        turno = 1
        while jogador["HP"] > 0 and computador["HP"] > 0:
            print(f"Turno: {turno}")
            print(f"Seu HP: {jogador['HP']}) | Computador HP: {computador['HP']}")

            while True:
                acao = input("Hora de atacar? [1] ou Curar? [2]")
                if acao in ["1", "2"]:
                    print("Ação inválida.")
                    break

                if acao == "1":
                    dano = max(0, jogador["ATQ"] - computador["DEF"])
                    computador["HP"] -= dano
                    print(f"Sua vez de atacar, o inimigo perdeu {dano} HP")

                else:
                    cura = random.randint(10, 30)
                    jogador["HP"] += cura
                    print(f"Você curou em {cura} HP")

                    acao_pc = random.choice(["atacar", "curar"])
                    if acao_pc == "atacar":
                        dano = max(0, computador["ATQ"] - jogador["DEF"])
                        jogador["HP"] -= dano
                        print(f"O inimigo atacou e você perdeu {dano} de HP")
                    else:
                        cura = random.randint(10, 30)
                        computador["HP"] += cura
                        print(f"Inimigo se cura em {cura} HP!")

                        turno += 1

                        if jogador["HP"] > computador["HP"]:
                            print("Você venceu, parabéns!")

                        elif jogador['HP'] <= 0 and computador["HP"] <= 0:
                            print("Empate!")

                        else:
                            print("Você foi derrotado!")