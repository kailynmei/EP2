from variaveis import CORES


def print_tabuleiro(mapa):
    print('\n   A B C D E F G H I J')

    for indice in range(len(mapa)):
        # printa coluna numeros - para cada linha
        if indice < 9:
            linha_formatada = str(indice + 1) + "  "
        else:
            # para 10 é diferente
            linha_formatada = str(indice + 1) + " "

        for celula in mapa[indice]:
            if celula == 'N':
                linha_formatada = linha_formatada + CORES['green'] + '░' + CORES['reset'] + " "
            else:
                linha_formatada = linha_formatada + celula + " "
        if indice < 9:
            linha_formatada = linha_formatada + "  " + str(indice + 1)
        else:
            # para 10 é diferente
            linha_formatada = linha_formatada + " " + str(indice + 1)

        print(linha_formatada)