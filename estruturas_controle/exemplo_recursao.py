def imprimir(maximo, atual):
    # Condição de Parada
    if atual >= maximo:
        print(atual)
        imprimir(maximo,atual + 1)


imprimir(10,1)
