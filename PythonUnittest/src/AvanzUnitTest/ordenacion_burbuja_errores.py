def burbuja_0(lista):
    """Algoritmo Ordenacion Burbuja
    PRUEBA ESTÁTICA. REQUISITO FUNCIONAL
    Esta función tiene 1 error de implementación

    Funcion que recibe por parametros una lista desordenada y que devuelve
    la misma lista pero con los elementos ya ordenados de menor a mayor 
    aplicando el algoritmo de ordenación por burbuja.
    See: 
        Documentacion: <link to https://es.wikipedia.org/wiki/Ordenamiento_de_burbuja>
    Args:
        lista: lista con los valores desordenados
    """
    for i in range(len(lista)):
        for j in range(len(lista)):
            if(lista[j] > lista[j+1]):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux

def burbuja_1(lista):
    """Algoritmo Ordenacion Burbuja
    PRUEBA DINAMICA. REQUISITO FUNCIONAL
    Esta función tiene 1 error de implementación        
    
    Funcion que recibe por parametros una lista desordenada y que devuelve
    la misma lista pero con los elementos ya ordenados de menor a mayor 
    aplicando el algoritmo de ordenación por burbuja.
    See: 
        Documentacion: <link to https://es.wikipedia.org/wiki/Ordenamiento_de_burbuja>
    Args:
        lista: lista con los valores desordenados
    """
    for i in range(len(lista)):
        for j in range(i, len(lista)-1):
            if(lista[j] > lista[j+1]):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux

def burbuja_2(lista):
    """Algoritmo Ordenacion Burbuja
    PRUEBA DINAMICA. REQUISITO NO FUNCIONAL
    Esta función tiene 1 error de rendimiento

    Funcion que recibe por parametros una lista desordenada y que devuelve
    la misma lista pero con los elementos ya ordenados de menor a mayor 
    aplicando el algoritmo de ordenación por burbuja.
    See: 
        Documentacion: <link to https://es.wikipedia.org/wiki/Ordenamiento_de_burbuja>
    Args:
        lista: lista con los valores desordenados
    """
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if(lista[j] > lista[j+1]):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux


def burbuja_3(lista):
    """Algoritmo Ordenacion Burbuja
    PRUEBA DINAMICA. REQUISITO NO FUNCIONAL
    Esta función tiene 1 error de aceptación

    Funcion que recibe por parametros una lista desordenada y que devuelve
    la misma lista pero con los elementos ya ordenados de menor a mayor 
    aplicando el algoritmo de ordenación por burbuja.
    See: 
        Documentacion: <link to https://es.wikipedia.org/wiki/Ordenamiento_de_burbuja>
    Args:
        lista: lista con los valores desordenados
    """
    for i in range(len(lista)):
        j = i+1
        for j in range(len(lista)):
            if(lista[i] > lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux