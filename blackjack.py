import os                         # Utilizado para limpar a tela
from random import randint        # Utilizado para gerar números aleatórios
from time import sleep            # Utilizado para gerar um tempo de espera entre as execuções


while True:
    os.system('cls') or None
    
    print('\nBem-Vindo ao Blackjack em Python!\n')
    print('Digite o número de jogadores (De 1 a 2 jogadores): ')
    print('Para sair digite 99.')
    njogadores = int(input(''))                        # Escolha do número de jogadores

    
    if njogadores == 99:                               # Encerra o programa
        print('\nObrigado por jogar, volte sempre!')
        break
 

    if njogadores == 1:                                # Versão para 1 jogador
        os.system('cls') or None
        print('Regras do jogo:\nPara ganhar você deve atingir um valor maior que o computador sem ultrapassar 21 pontos podendo parar após cada jogada.')
        print('\nDigite "start" para começar.') 
        inicio = str(input(''))                        # Início do jogo
        if inicio == 'start':  
            totalj = 0
            totalj += randint(1,10)
            print(f'\nVocê começa com {totalj}')
            while True:
                if totalj > 21:
                    print('Você estourou!!!')
                    break
                print('\nDeseja continuar jogando? [S/N]')
                opt = str(input(''))
                if opt == 'S' or opt == 's':
                    jogada = randint(1,10)
                    totalj = totalj + jogada
                    os.system('cls') or None
                    print(f'\nVocê tirou {jogada} e possui um total de {totalj}')

                elif opt == 'N' or opt == 'n':
                    break

                else:
                    print('\nOpção inválida, digite S ou N.')
            print(f'Você ficou com um total de {totalj}\n')
            sleep(2)
            print(f'Computador: Vejo que você ficou com {totalj}, agora é minha vez.')
            sleep(2)
            totalc = randint(1,10)
            print(f'Computador: Eu começo com {totalc}')
            sleep(2)
            while totalc < 18:
                print(f'Computador: Vou continuar, acho que ainda consigo um valor maior.')
                sleep(2)
                jogada = randint(1,10)
                totalc = totalc + jogada
                print(f'\nComputador: Tirei {jogada} e meu total é {totalc}')
                sleep(2)

            if totalc > 21:
                print('\nComputador: Ops, estourei.')
                sleep(2)
            elif totalc <= 21:
                print(f'\nComputador: Parei pois fiquei com um total de {totalc}')        
                sleep(2)

            if totalj == totalc:
                print('\nComputador: Empatamos. Aff quero revanche!')
            elif totalj > 21:
                print('\nComputador: Você estourou, eu venci!\nMais sorte na próxima!')
            elif totalc > 21:
                print('\nComputador: Aff estourei. Você venceu.\nNa próxima eu ganho!')
            elif totalj > totalc:
                print('\nComputador: Você chegou mais perto de 21. Você venceu!\nNa próxima eu com certeza ganho, me aguarde!')
            elif totalj < totalc:
                print('\nComputador: Eu cheguei mais perto de 21. Eu venci!\nMais sorte na próxima hahaha!')
            sleep(5)


    if njogadores == 2:                                # Versão para dois jogadores                         
        os.system('cls') or None
        print('Regras do jogo:\nPara ganhar você deve atingir um valor maior que o seu adversário sem ultrapassar 21 pontos podendo parar após cada jogada.')
        print('\nDigite "start" para começar.') 
        inicio = str(input(''))                        # Início do jogo
        if inicio == 'start':
            totalj1 = 0
            totalj1 += randint(1,10)
            totalj2 = 0
            totalj2 += randint(1,10)
            os.system('cls') or None
            print(f'Jogador 1: Você começa com {totalj1}')                      # Jogador 1
            
            while True:
                if totalj1 > 21:
                    print('Jogador 1: Você estourou!!!')
                    sleep(2)
                    break
                print('\nJogador 1: Deseja continuar jogando? [S/N]')
                opt = str(input(''))
                if opt == 'S' or opt == 's':
                    jogada = randint(1,10)
                    totalj1 += jogada
                    os.system('cls') or None
                    print(f'\nJogador 1: Você tirou {jogada} e possui um total de {totalj1}')
                elif opt == 'N' or opt == 'n':
                    break
                else:
                    print('\nOpção inválida, digite S ou N.')
            os.system('cls') or None

            print(f'\nJogador 1: Você ficou com um total de {totalj1}\n')
            sleep(2)
            
            print('Vez do jogador 2')                                          # Jogador 2
            sleep(2)                                           
            print(f'\nJogador 2: Você começa com {totalj2}')
            
            while True:
                if totalj2 > 21:
                    print('\nJogador 2: Você estourou!!!')
                    sleep(2)
                    break
                print('\nJogador 2: Deseja continuar jogando? [S/N]')
                opt = str(input(''))
                if opt == 'S' or opt == 's':
                    jogada = randint(1,10)
                    totalj2 += jogada
                    os.system('cls') or None
                    print(f'\nJogador 2: Você tirou {jogada} e possui um total de {totalj2}')
                elif opt == 'N' or opt == 'n':
                    break
                else:
                    print('\nOpção inválida, digite S ou N.')

            
            print(f'\nJogador 2: Você ficou com um total de {totalj2}\n')
            sleep(2)
            os.system('cls') or None
            print(f'Total jogador 1: {totalj1}')
            print(f'Total jogador 2: {totalj2}')
            sleep(3)
            
            if totalj1 == totalj2:
                print('\nVocês empataram. Tentem uma revanche.')
            elif totalj1 > 21 and totalj2 > 21:
                print('\nVocês estouraram!\nMais sorte na próxima!')
            elif totalj1 > 21:
                print('\nJogador 1 estourou.\nJogador 2 venceu.')
            elif totalj2 > 21:
                print('\nJogador 2 estourou.\nJogador 1 venceu.')
            elif totalj1 > totalj2:
                print('\nJogador 1 chegou mais perto de 21.\nJogador 1 venceu!')
            elif totalj2 > totalj1:
                print('\nJogador 2 chegou mais perto de 21.\nJogador 2 venceu!')
            sleep(5)
            
            

    if njogadores < 1 or njogadores > 2:               # Número inexistente de jogadores
        print('Número de jogadores inválido, escolha um valor entre 1 e 2.')
        sleep(3)

    
