import random
import os

maoJogador1 = []
maoJogador2 = []

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
    # monteDeEspera é reiniciado aqui,  para não persistir entre partidas outras possveis
    monteDeEspera = []

    # Validação caso digite outro valor
    while True:
        opcaoJogo = input("1 - Single Player\n2 - Multiplayer\n3 - Sair\nComo você deseja jogar? ")
    
        if opcaoJogo in ["1", "2", "3"]:
            break # A entrada é válida, então quebra o loop e segue o jogo!
        # Se o código não parou no break acima, ele cai aqui no erro naturalmente
        print("Entrada inválida! Por favor, digite apenas números (1, 2 ou 3).\n")

    random.shuffle(baralhos)

    maoJogador1 = baralhos[0: len(baralhos)//2]
    maoJogador2 = baralhos[len(baralhos)//2: len(baralhos)]

    opcaoJogo = int(opcaoJogo)

    # Encerra o programa
    if opcaoJogo == 3:
        print("Saindo do jogo. Bye!\n")
        break

    if opcaoJogo == 1:
        print("Você escolheu a opção Single Player\n")
        
        turno = 1 

        while len(maoJogador1) > 0 and len(maoJogador2) > 0:
            print(f"PLACAR QTD Cartas - Jogador 1: {len(maoJogador1)} | Computador: {len(maoJogador2)}\n")
            
            if turno == 1:
                # É bom mostrar a carta do jogador apenas quando for a vez dele
                print("CARTA TOPO - JOGADOR 1")
                for i in range(len(gabarito)):
                    print(f"{gabarito[i]}: {maoJogador1[0][i]}")
                print("\n")

                print("---ATENÇÃO! É A SUA VEZ DE ESCOLHER O ATRIBUTO---\n")
                escolhaValida = False
                1
                while True:
                    escolhaAtributoStr = input("Quem escolher um atributo de valor maior vence a rodada.\n1 - Velocidade\n2 - Tanque\n3 - Ano\nQual atributo você irá escolher? ")
                    
                    if escolhaAtributoStr in ["1", "2", "3"]:
                        escolhaAtributoJogador = int(escolhaAtributoStr)
                        break # sai do loop se for vdd
                        
                    print("\nOpção inválida! Escolha 1, 2 ou 3.\n")
            else:
                # Turno do computador: carta do Jogador 1 não é exibida 
                print("---ATENÇÃO! É A VEZ DO COMPUTADOR ESCOLHER O ATRIBUTO---\n")
                escolhaAtributoJogador = random.randint(1, 3)

                # tributo do CPU revelado apenas após a pausa, não antes
                input("Pressione Enter para ver a escolha do Computador e ir para o embate: ")
                print(f"\nO Computador analisou a carta dele e escolheu o atributo: {gabarito[escolhaAtributoJogador]}\n")

            # Pegando os valores para comparar
            valorEscolhidoJogador = maoJogador1[0][escolhaAtributoJogador]
            valorEscolhidoComputador = maoJogador2[0][escolhaAtributoJogador]

            cartaJ1 = maoJogador1[0]
            cartaJ2 = maoJogador2[0]

            if valorEscolhidoJogador > valorEscolhidoComputador:
                print(f"\nComparativo Cartas: Jogador 1 ({valorEscolhidoJogador}) x Computador ({valorEscolhidoComputador})")
                print("Você venceu a rodada! A próxima vez de escolher será sua.\n")
                
                maoJogador2.pop(0)
                maoJogador1.pop(0)
                maoJogador1.append(cartaJ2)
                maoJogador1.append(cartaJ1)

                turno = 1 # Garante que o jogador 1 joga a próxima

                # Entregar o monte de espera para o Jogador 1
                if len(monteDeEspera) > 0:
                    for carta in monteDeEspera:
                        maoJogador1.append(carta)
                    monteDeEspera = [] 

            elif valorEscolhidoComputador > valorEscolhidoJogador:
                print(f"\nComparativo Cartas: Jogador 1 ({valorEscolhidoJogador}) x Computador ({valorEscolhidoComputador})")
                print("O Computador venceu a rodada! A próxima vez de escolher será dele.\n")
                
                maoJogador2.pop(0)
                maoJogador1.pop(0)
                maoJogador2.append(cartaJ1)
                maoJogador2.append(cartaJ2)

                turno = 2 # Passa o turno para o computador

                # Entregar o monte de espera para o Computador
                if len(monteDeEspera) > 0:
                    for carta in monteDeEspera:
                        maoJogador2.append(carta)
                    monteDeEspera = [] 
            
            else:
                print(f"\nComparativo Cartas: Jogador 1 ({valorEscolhidoJogador}) x Computador ({valorEscolhidoComputador})")
                print("Ocorreu um empate nessa rodada...\nAs cartas topo dos dois jogadores serão adicionadas no monte de espera!")
                print("Como houve empate, o turno de escolha permanece com o último a jogar.\n")
                
                maoJogador1.pop(0)
                maoJogador2.pop(0)
                monteDeEspera.append(cartaJ1)
                monteDeEspera.append(cartaJ2)
                
            input("Pressione Enter para a próxima rodada: ") 
            # Limpeza de tela usando a bibliotec os.system para limpar o terminal
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n")
            print("=" * 50)

        # Finalização da partida REGRAS: jogo termina quando um jogador possuir todas as cartas) 
        if len(maoJogador1) == 0:
            print("Fim de jogo! O Computador é o vencedor absoluto!\n")
        else:
            print("Fim de jogo! Você é o vencedor absoluto!\n")
            
        # Faz o programa  volta ao menu
        input("Pressione Enter para voltar ao menu: ")
        # Refreshde tela ao voltar ao menu
        os.system('cls' if os.name == 'nt' else 'clear')

# Lógica do MultiPlayer
    elif opcaoJogo == 2:
        print("Você escolheu a opção Multiplayer\n")
        
        turno = 1

        while len(maoJogador1) > 0 and len(maoJogador2) > 0:
            print(f"Placar Qtd Cartas - Jogador 1: {len(maoJogador1)} | Jogador 2: {len(maoJogador2)}\n")
            
            if turno == 1:

                # A sequência em caso do jogador 1 ganhar
                vez = ""
                while vez != "1":
                    vez = input("Vez do Jogador 1 visualizar sua carta topo, digite 1 para ver a carta: ")
                    
                print("CARTA TOPO - JOGADOR 1")
                for i in range(len(gabarito)):
                    print(f"{gabarito[i]}: {maoJogador1[0][i]}")
                print("\n")
                
                print("---ATENÇÃO! É A SUA VEZ DE ESCOLHER O ATRIBUTO JOGADOR 1---\n")
                escolhaValida = False
                while escolhaValida == False:
                    escolhaAtributoStr = input("Quem escolher um atributo de valor maior vence a rodada.\n1 - Velocidade\n2 - Tanque\n3 - Ano\nQual atributo você irá escolher? ")
                    if escolhaAtributoStr == "1" or escolhaAtributoStr == "2" or escolhaAtributoStr == "3":
                        escolhaAtributoJogador = int(escolhaAtributoStr)
                        escolhaValida = True
                    else:
                        print("\nOpção inválida! Escolha 1, 2 ou 3.\n")
                
                input("\nPressione Enter para esconder a carta e passar a vez para o Jogador 2: ")
                # Limpeza de tela usando a biblioteca os.system para o Jogador 2 não ver a carta do Jogador 1
                os.system('cls' if os.name == 'nt' else 'clear')

                vez = ""
                while vez != "2":
                    vez = input("Vez do Jogador 2 visualizar sua carta topo, digite 2 para ver a carta: ")
                    
                print("CARTA TOPO - JOGADOR 2")
                for i in range(len(gabarito)):
                    print(f"{gabarito[i]}: {maoJogador2[0][i]}")
                print("\n")
                
                input("\nPressione Enter para ir para o embate: ")
                # Limpeza de tela usando a bibliotec os.system antes de mostrar o resultado
                os.system('cls' if os.name == 'nt' else 'clear')

            else:

                # A sequência em caso do jogador 2 ganhar
                vez = ""
                while vez != "2":
                    vez = input("Vez do Jogador 2 visualizar sua carta topo, digite 2 para ver a carta: ")
                    
                print("CARTA TOPO - JOGADOR 2")
                for i in range(len(gabarito)):
                    print(f"{gabarito[i]}: {maoJogador2[0][i]}")
                print("\n")
                
                print("---ATENÇÃO! É A SUA VEZ DE ESCOLHER O ATRIBUTO JOGADOR 2---\n")
                escolhaValida = False
                while escolhaValida == False:
                    escolhaAtributoStr = input("Quem escolher um atributo de valor maior vence a rodada.\n1 - Velocidade\n2 - Tanque\n3 - Ano\nQual atributo você irá escolher? ")
                    if escolhaAtributoStr == "1" or escolhaAtributoStr == "2" or escolhaAtributoStr == "3":
                        escolhaAtributoJogador = int(escolhaAtributoStr)
                        escolhaValida = True
                    else:
                        print("\nOpção inválida! Escolha 1, 2 ou 3.\n")
                
                input("\nPressione Enter para esconder a carta e passar a vez para o Jogador 1: ")
                # Limpeza de tela usando a biblioteca os.system para o Jogador 1 não ver a carta do Jogador 2
                os.system('cls' if os.name == 'nt' else 'clear')

                vez = ""
                while vez != "1":
                    vez = input("Vez do Jogador 1 visualizar sua carta topo, digite 1 para ver a carta: ")
                    
                print("CARTA TOPO - JOGADOR 1")
                for i in range(len(gabarito)):
                    print(f"{gabarito[i]}: {maoJogador1[0][i]}")
                print("\n")
                
                input("\nPressione Enter para ir para o embate: ")
                # Limpeza de tela usando a bibliotec os.system antes de mostrar o resultado
                os.system('cls' if os.name == 'nt' else 'clear')
            
            # mesmo terminal, a variável de escolha mantém
            valorEscolhidoJ1 = maoJogador1[0][escolhaAtributoJogador]
            valorEscolhidoJ2 = maoJogador2[0][escolhaAtributoJogador]

            cartaJ1 = maoJogador1[0]
            cartaJ2 = maoJogador2[0]
            
            print(f"O atributo escolhido para a disputa foi: {gabarito[escolhaAtributoJogador]}")

            if valorEscolhidoJ1 > valorEscolhidoJ2:
                print(f"\nComparativo Cartas: Jogador 1 ({valorEscolhidoJ1}) x Jogador 2 ({valorEscolhidoJ2})")
                print("Jogador 1 venceu a rodada! A próxima vez de escolher será dele.\n")
                
                maoJogador2.pop(0)
                maoJogador1.pop(0)
                maoJogador1.append(cartaJ2)
                maoJogador1.append(cartaJ1)

                turno = 1 # Garantia que o Jogador 1 joga a próxima

                # Entregar o monte para o Jogador 1
                if len(monteDeEspera) > 0:
                    for carta in monteDeEspera:
                        maoJogador1.append(carta)
                    monteDeEspera = [] 

            elif valorEscolhidoJ2 > valorEscolhidoJ1:
                print(f"\nComparativo Cartas: Jogador 1 ({valorEscolhidoJ1}) x Jogador 2 ({valorEscolhidoJ2})")
                print("Jogador 2 venceu a rodada! A próxima vez de escolher será dele.\n")
                
                maoJogador2.pop(0)
                maoJogador1.pop(0)
                maoJogador2.append(cartaJ1)
                maoJogador2.append(cartaJ2)

                turno = 2 # Passa o turno para o Jogador 2

                # Entregar monte para o Jogador 2
                if len(monteDeEspera) > 0:
                    for carta in monteDeEspera:
                        maoJogador2.append(carta)
                    monteDeEspera = [] 
            
            else:
                print(f"\nComparativo Cartas: Jogador 1 ({valorEscolhidoJ1}) x Jogador 2 ({valorEscolhidoJ2})")
                print("Ocorreu um empate nessa rodada...\nAs cartas topo dos dois jogadores serão adicionadas no monte de espera!")
                print("Como houve empate, o turno de escolha permanece com o último a jogar.\n")
                
                maoJogador1.pop(0)
                maoJogador2.pop(0)
                monteDeEspera.append(cartaJ1)
                monteDeEspera.append(cartaJ2)
                
            input("Pressione Enter para a próxima rodada: ") 
            # Limpeza de tela usando a biblioteca os.system para o Jogador 2 não ver o resultado anterior
            os.system('cls' if os.name == 'nt' else 'clear')

        # Finalização da partida
        if len(maoJogador1) == 0:
            print("Fim de jogo! O Jogador 2 é o vencedor absoluto!\n")
        else:
            print("Fim de jogo! O Jogador 1 é o vencedor absoluto!\n")
            
        input("Pressione Enter para voltar ao menu: ")
        # Rresh de tela ao voltar ao menu
        os.system('cls' if os.name == 'nt' else 'clear')