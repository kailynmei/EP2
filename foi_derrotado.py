# exercicio 4
def foi_derrotado(mapa):
    for lista in mapa:
        if 'N' in lista:
            return False
    return True