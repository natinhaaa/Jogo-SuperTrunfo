import random
import os
import time

maoJogador1 = []
maoJogador2 = []
monteDeEspera = []
baralhos = [
    ["Toyota Yaris Cross", 175, 36, 2024],
    ["Ferrari F40", 324, 120, 1987],
    ["Lamborghini Aventador", 350, 90, 2011],
    ["Bugatti Chiron", 420, 100, 2016],
    ["Porsche 911", 310, 64, 2023],
    ["McLaren P1", 350, 72, 2013],
    ["Audi R8", 330, 83, 2021],
    ["BYD Song Plus", 170, 60, 2023]
]
gabarito = ["Nome", "Velocidade (km/h)", "Tanque (litros)", "Ano (int)"]

while True:
    opcaoJogo = int(input("1 - Single Player\n2 - Multiplayer\n3 - Sair\nComo você deseja jogar? "))
    random.shuffle(baralhos) # Embaralha as listas dentro da lista baralhos

    # Divisão inteira da quantidade das listas dentro de baralhos, caso a quantidade seja ímpar na divisão //2, ele arredonda pro número inteiro sem decimal
    # O fatiamento usamos para ele copiar os valores da lista baralhos dentro das listas das mãos dos jogadores, e como deve separar a mesma quantidade de cartas para os dois jogadores, por exemplo pro jogador1, pegamos do começo da lista (0:) até a metade (len(baralhos)//2), o mesmo pro jogador2, mas da metade (len(baralhos)//2) até o final (len(baralhos))
    maoJogador1 = baralhos[0: len(baralhos)//2]
    maoJogador2 = baralhos[len(baralhos)//2: len(baralhos)]

    if opcaoJogo == 1:
        print("Você escolheu a opção Single Player")

        while len(maoJogador1) > 0 and len(maoJogador2) > 0:
            print("CARTA TOPO - JOGADOR 1")
            for i in range(len(gabarito)):
                print(f"{gabarito[i]}: {maoJogador1[0][i]}")
            print("\n")
            
            escolhaAtributoJogador = int(input("Agora você irá escolher um atributo da sua carta do topo!\nQuem escolher um atributo de valor maior vence a rodada.\n1 - Velocidade\n2 - Tanque\n3 - Ano\nQual atributo você irá escolher? "))

            valorEscolhidoJogador = maoJogador1[0][escolhaAtributoJogador]
            
            # O valor dos atributos que estão disponíveis pro computador escolher estão entre 1 ("Velocidade") e len(gabarito)-1 (ou seja 4-1=3 (até o o atributo "Ano"))
            valorEscolhidoComputador = maoJogador2[0][random.randint(1,len(gabarito)-1)]

            cartaJ1 = maoJogador1[0]
            cartaJ2 = maoJogador2[0]

            if valorEscolhidoJogador > valorEscolhidoComputador:
                maoJogador2.pop(0)
                maoJogador1.pop(0)
                maoJogador1.append(cartaJ2)
                maoJogador1.append(cartaJ1)

            elif valorEscolhidoComputador > valorEscolhidoJogador:
                maoJogador2.pop(0)
                maoJogador1.pop(0)
                maoJogador2.append(cartaJ1)
                maoJogador2.append(cartaJ2)
            
            else:
                maoJogador1.pop(0)
                maoJogador2.pop(0)
                monteDeEspera.append(cartaJ1)
                monteDeEspera.append(cartaJ2)
            

    elif opcaoJogo == 2:
        print("Você escolheu a opção Multiplayer")

        while len(maoJogador1) > 0 and len(maoJogador2) > 0:
            # Coloquei esse input para não aparecer as cartas topos dos dois jogadores de uma vez, assim eles jogam sem saber a carta um do outro
            vez = input("Vez do Jogador 1 visualizar sua carta topo, pressione Enter para ver a carta: ")
            print("CARTA TOPO - JOGADOR 1")
            for i in range(len(gabarito)):
                print(f"{gabarito[i]}: {maoJogador1[0][i]}")
            
            # Coloquei tipo um temporizador pro jogador visualizar a carta dele e depois o os.system('cls') para apagar o conteúdo do terminal e o próximo jogador não conseguir ver a carta do adversário. Não precisa, mas faz mais sentido usar isso pros dois não ficarem olhando pra carta do outro
            time.sleep(10)
            os.system('cls')

            print("\n")

            vez = input("Vez do Jogador 2 visualizar sua carta topo, pressione Enter para ver a carta: ")
            print("CARTA TOPO - JOGADOR 2")
            for i in range(len(gabarito)):
                print(f"{gabarito[i]}: {maoJogador2[0][i]}")
            time.sleep(10)
            os.system('cls')
            


    elif opcaoJogo == 3:
        print("Você escolheu sair")
        exit()

    else:
        print("Opção inválida, tente novamente")