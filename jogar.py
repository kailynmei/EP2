import time, random
from variaveis import CORES, LETRAS
from print_tabuleiro import print_tabuleiro
from posicao_suporta import posicao_suporta
from foi_derrotado import foi_derrotado
from cria_mapa import cria_mapa

def Jog_aloca_navios(mapa_jogador, navios_jog):
    i = 0
    while i < len(navios_jog):
        # o "end=' '" não vai deixar ele pular a linha para a proxima
        print('\n- Sua frota (blocos) --> [', end='')
        contador = 0
        tamanho = len(navios_jog) 
        while contador < tamanho:
            navio = navios_jog[contador]
            if contador == i:
                # coloca a cor azul no navio
                print(CORES['blue'] + str(navio) + CORES['reset'], end='')
            else:
                print(str(navio), end='')
            # checa se coloca vírgula ou não
            if contador < tamanho - 1:
                print(', ', end='')
            contador += 1
        print(']')

        while True:
            letra = input('\nInforme a Letra: ').upper()
            try:
                linha = int(input('\nInforme a Linha: '))
            except:
                print("linha invalida, digite novamente")
                linha = int(input("\nInofrme a Linha: "))
            orientacao = input('Informe a Orientação  [v|h]: ')
            # corrigir com o index
            linha -= 1
            idx = 0
            for let in LETRAS:
                if let == letra:
                    idx = LETRAS.index(letra)
            coluna = idx   
            if posicao_suporta(mapa_jogador, navios_jog[i], linha, coluna, orientacao) == True:
                    incremento_linha = 0
                    incremento_coluna = 0
                    if orientacao == 'v':
                        incremento_linha = 1
                    else:
                        incremento_coluna = 1  
                    for vezes in range(navios_jog[i]):
                        mapa_jogador[linha + vezes * incremento_linha][coluna + vezes * incremento_coluna] = 'N'

                    print_tabuleiro(mapa_jogador)
                    i += 1
                    break
            else:
                print('\nPosição Inválida! Informe outras coordendas.')
    return mapa_jogador
    

# colocando o código para jogar dentro da função porque ai posso chamar de 
# novo quando quiser jogar novamente
def Jogar(mapa_computador, mapa_jogador):
    time.sleep(1)
    print('\nPrepara-se para começar a guerra!')
    time.sleep(1)

    mapa_computador_aparece = cria_mapa(10)
    while True:

        letra = input('\nInforme a Letra: ').upper()
        try:
            linha = int(input('\nInforme a Linha: '))
        except:
            print("linha invalida, digite novamente")
            linha = int(input("\nInofrme a Linha: "))
        # corrigir com o index
        linha -= 1
        idx = 0
        for let in LETRAS:
            if let == letra:
                idx = LETRAS.index(letra)
        coluna = idx
        if mapa_computador[linha][coluna] == 'N':
            mapa_computador[linha][coluna] = 'X'
            mapa_computador_aparece[linha][coluna] = CORES['red'] + '▒' + CORES['reset']
        elif mapa_computador[linha][coluna] == ' ':
            mapa_computador_aparece[linha][coluna] = CORES['blue'] + '▒' + CORES['reset']

        print('\nTABULEIRO DO COMPUTADOR:')
        print_tabuleiro(mapa_computador_aparece)
        if foi_derrotado(mapa_computador) is True:
            print('Você ganhou!')
            break

        n = len(mapa_jogador[0])
        linha_comp = random.randint(0, n-1)
        letra_comp = random.randint(0, n-1)

        if mapa_jogador[linha_comp][letra_comp] == 'N':
            mapa_jogador[linha_comp][letra_comp] = CORES['red'] + '▒' + CORES['reset']
        elif mapa_jogador[linha_comp][letra_comp] == ' ':
            mapa_jogador[linha_comp][letra_comp] = CORES['blue'] + '▒' + CORES['reset']
        
        print('\nTABULEIRO DO JOGADOR:')
        print_tabuleiro(mapa_jogador)
        if foi_derrotado(mapa_jogador) is True:
            print('Você foi derrotado!')
            break
