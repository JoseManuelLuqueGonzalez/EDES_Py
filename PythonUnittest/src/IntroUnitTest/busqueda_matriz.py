def busqueda_matriz_error(matriz, x):
    """Error en busqueda matriz
    En esta funcion existen 3 errores.
    2 errores de implementacion (Funcionales)
    1 error de aceptación (No funcionales)
    """
    encontrado = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (matriz[i][j] == x):
                encontrado = True
    return encontrado





def busqueda_matriz_no_eficiente(matriz, x):
    """Eficiencia baja
    En esta función se han solventado los errores.
    Hay varias maneras de hacer al programa más eficiente y usable(No funcionales)
    """
    for fila in matriz:
        for celda in fila:
            if (celda == x):
               return True
    return False





def busqueda_matriz(matriz, x):
    """Busqueda matriz
    Funcion que busca dentro de una matriz un elemento dado

    Args:
        matriz: matriz con valores
        x: valor a buscar en la matriz
    return:
        True: se ha encontrado el valor en la matriz
        False: no se ha encontrado el valor en la matriz
    """
    for fila in matriz:
        for celda in fila:
            if (celda == x):
                return True
    return False



if __name__ == "__main__":
    matriz = [[1,2,4],[7,3,5],[6,8,9]]
    val = 9
    if(busqueda_matriz(matriz, val)):
        print(f"Se ha encontrado {val}")
    else:
        print(f"{val} no se encuentra en la matriz")