# BATLHA NAVAL POR Kailyn Ng, Davi Korber e Fernaanda Ribeiro
import time
import random
from cria_mapa import cria_mapa
from posicao_suporta import posicao_suporta
from aloca_navios import aloca_navios
from foi_derrotado import foi_derrotado
from loading import loading
from print_tabuleiro import print_tabuleiro
from variaveis import PAISES, CONFIGURACAO, LETRAS, CORES
from jogar import Jog_aloca_navios, Jogar    


while True:
    # título
    print('\n- - - - - - - - - - - - - - - - - - - - - - - - -')
    print('|                                              |')
    print('|            \u001b[33m> JOGO BATALHA NAVAL <\u001b[0m            |')
    print('|                                              |')
    print('- - - - - - - - - - - - - - - - - - - - - - - - -')
    print()
    loading()

    # comeco do jogo
    terminal_paises = '\n\n'
    for nacao, navios_comp in PAISES.items():
        terminal_paises += f'{nacao}:\n'
        for navio, quantidade in navios_comp.items():
            terminal_paises += f'  {quantidade} {navio}\n'
        terminal_paises += '\n' # pula linha
    print(terminal_paises, end='')

    paises = ['Brasil', 'Austrália', 'Japão', 'Rússia', 'França']
    while True:
        pais_jogador = input('Escolha o país que você deseja jogar: ')
        # checa se tem esse país 
        if pais_jogador not in paises:
            print('escolha um país válido')
        else:
            break

    print('- JOGADOR -> ' + pais_jogador + '.')
    paises.remove(pais_jogador)
    pais_computador = random.choice(paises)
    print('- COMPUTADOR -> ' + pais_computador + '.')
    print('\nAloque os navios da sua frota...')

    # fazendo lista de navios - blocos para colocar na função de alocar navios para o computador
    navios_comp = []
    for navio, quantidade in PAISES[pais_computador].items():
        for vezes in range(quantidade):
            blocos = CONFIGURACAO[navio]
            navios_comp.append(blocos)

    #  MSM COISA QUE FIZEMOS ANTES MAS P/ O JOGADOR
    # fazendo lista de navios - blocos para colocar na função de alocar navios para o jogador
    navios_jog = []
    for navio, quantidade in PAISES[pais_jogador].items():
        for vezes in range(quantidade):
            blocos = CONFIGURACAO[navio]
            navios_jog.append(blocos)
    mapa_jogador = cria_mapa(10)
    print_tabuleiro(mapa_jogador)

    # criando o mapa do comp e alocando os navios
    mapa = cria_mapa(10)
    mapa_computador = aloca_navios(mapa, navios_comp)

    # DESCOMENTAR SE QUISER VER O LOCAL DOS NAVIOS DO COMP PARA FACILITAR TESTAR O CÓDIGO
    # print('Tabuleiro Computador:')
    # print_tabuleiro(mapa_computador)
    # print('\n---------------------------------------')

    Jog_aloca_navios(mapa_jogador, navios_jog)
    Jogar(mapa_computador, mapa_jogador)
    de_novo = input('Gostaria de Jogar novamente (sim/nao)')
    if de_novo == 'nao':
        break
    # vai reinicar tudo
    