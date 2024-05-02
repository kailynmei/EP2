# exercicio 2
def posicao_suporta(mapa, tamanho_navio, linha, coluna, orientação):

    if orientação == 'v':
        lista_coluna = []
        for lista_linha in mapa:
            lista_coluna.append(lista_linha[coluna]) # append dos valores das linhas no index da coluna

        lista_coluna = lista_coluna[linha:]  # cortar a lista da coluna pra comecar a partir do index da linha
        if tamanho_navio > len(lista_coluna):
            # mais bloco do que espaço
            return False
        i = 0
        # passar pela lista coluna quantas vezes tiver de blocos, checando se tem Navio
        for espaco in lista_coluna:
            if i < tamanho_navio:
                if espaco == 'N':
                    return False
                i += 1
        # não achou navio
        return True
        
    elif orientação == 'h':
        lista_linha = mapa[linha]   # lista no indice da linha
        lista_linha = lista_linha[coluna:] # cortar pra comecar a partir da coluna 
        if tamanho_navio > len(lista_linha):
            return False
        i = 0
        # passar pela lista coluna quantas vezes tiver de blocos, checando se tem Navio
        for espaco in lista_linha:
            if i < tamanho_navio:
                if espaco == 'N':
                    return False
                i += 1
        # não achou navio
        return True