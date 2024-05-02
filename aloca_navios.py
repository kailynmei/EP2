import random
from posicao_suporta import posicao_suporta

# exercicio 3
def aloca_navios(mapa, blocos):
    n = len(mapa[0])

    while len(blocos) > 0:
        blocos_navio = blocos[0]
        blocos.remove(blocos_navio)

        while True: # se não for valido reinicia
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(['h', 'v'])

            if posicao_suporta(mapa, blocos_navio, linha, coluna, orientacao):
                if orientacao == 'v':
                    for i in range(linha, linha + blocos_navio):
                        # faz isso o numero de vezes que tem de blocos aumentando o 
                        # index da linha ja que é vertical
                        mapa[i][coluna] = 'N'
                elif orientacao == 'h':
                    # mesma coisa que o de cima mas na coluna
                    for i in range(coluna, coluna + blocos_navio):
                        mapa[linha][i] = 'N'
                break
            else:
                continue
    return mapa