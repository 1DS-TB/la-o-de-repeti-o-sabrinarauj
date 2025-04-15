import random

print("Bem-vindo ao jogo! - Duelo de Heróis")

jogador1 = {
    #HP: Vida
    #DEF: Defesa
    #ATQ: Ataque
    "HP": random.randint(200, 1000),
    "ATQ": random.randint(1, 50),
    "DEF": random.randint(1, 50),
    "CRITICO": random.randint(10, 100)
}
jogador2 = {
    "HP": random.randint(200, 1000),
    "ATQ": random.randint(1, 50),
    "DEF": random.randint(1, 50),
    "CRITICO": random.randint(10, 100)
}
cpu = {
    "HP": random.randint(200, 1000),
    "ATQ": random.randint(1, 50),
    "DEF": random.randint(1, 50)
}

while True:
    print("=== Menu ===\n")
    print("1-Iniciar jogo\n")
    print("2-Jogar Multiplayer")
    print("3-Sair\n")
    escolha = input("Escolha uma da opções acima: ")

    if escolha == "3":
        print("Você saiu do jogo.")
        break

    elif escolha == "1":
        print("O Duelo começou...\n")
        print("Você")
        print(f"HP: {jogador1['DEF']}")
        print("Inimigo (computador)")
        print(f"HP: {cpu['HP']}")
        print(f"Ataque: {cpu['ATQ']} DEF: {cpu['DEF']}\n")

        turno = 1
        while jogador1["HP"] > 0 and cpu["HP"] > 0:
            print(f"Turno: {turno}")
            print(f"Seu HP: {jogador1['HP']}) | Computador HP: {cpu['HP']}")

            while True:
                acao = input("Hora de atacar? [1] Poção de Cura? [2] Poção de Regeneração? [3]")
                if acao in ["1", "2", "3"]:
                    print("Ação inválida.")
                    break

                if acao == "1":
                    dano = max(0, jogador1["ATQ"] - cpu["DEF"])
                    cpu["HP"] -= dano
                    print(f"Sua vez de atacar, o inimigo perdeu {dano} HP")

                else:
                    cura = random.randint(10, 30)
                    jogador1["HP"] += cura
                    print(f"Você curou em {cura} HP")

                    acao_pc = random.choice(["atacar", "curar"])
                    if acao_pc == "atacar":
                        dano = max(0, cpu["ATQ"] - jogador1["DEF"])
                        jogador1["HP"] -= dano
                        print(f"O inimigo atacou e você perdeu {dano} de HP")
                    else:
                        cura = random.randint(10, 30)
                        cpu["HP"] += cura
                        print(f"Inimigo se cura em {cura} HP!")

                        turno += 1

                        if jogador1["HP"] > cpu["HP"]:
                            print("Você venceu, parabéns!")

                        elif jogador1['HP'] <= 0 and cpu["HP"] <= 0:
                            print("Empate!")

                        else:
                            print("Você foi derrotado!")
                turno = 2
                while jogador1["HP"] > 0 and jogador2["HP"] > 0:
                    print(f"Turno: {turno}")
                    print(f"Jogador 1 - HP: {jogador1['HP']} | Jogador 2 - HP: {jogador2['HP']}")

                    while True:
                        acao = input("Hora de atacar? [1] ou Curar? [2] Poção de Regeneração? [3]")
                        break
                    if acao in ["1", "2", "3"]:
                        print("Ação inválida")
                    elif acao == "1":
                        dano = max(0, jogador1["ATQ"] - jogador2["DEF"])
                        jogador2["HP"] -= dano
                        print(f"Você atacou! O jogador 2 perdeu {dano} HP")

                    else:
                      print(f"Turno: {turno}")
                      print(f"Jogador 1 - HP: {jogador1['HP']} | Jogador 2 - HP: {jogador2['HP']}")

                      while True:
                          acao = input("Hora de atacar? [1] ou Curar? [2] Poção de Regeneração? [3]")
                          break
                    if acao in ["1", "2", "3"]:
                        print("Ação inválida")
                    elif acao == "1":
                        dano = max(0, jogador2["ATQ"] - jogador2["DEF"])
                        jogador1["HP"] -= dano
                        print(f"Você atacou! O jogador 1 perdeu {dano} HP")

                        #Finalizar o desafio e arrumar o código