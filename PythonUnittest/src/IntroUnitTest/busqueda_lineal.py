def busqueda_lineal_mal(lista, x):
    """Busqueda lineal
    Funcion que busca dentro de una lista un valor dado.
    Existe un error de implementación en esta función (prueba funcional)
    Args:
        lista: lista con valores
        x: valor a buscar en la lista
    return:
        True: se ha encontrado el valor en la lista
        False: no se ha encontrado el valor en la lista
    """
    encontrado = False
    for i in range(len(lista)):
        if(lista[i] == x):
            encontrado = True

    return encontrado

    

    
def busqueda_lineal_no_eficiente(lista, x):
    """Busqueda lineal
    Funcion que busca dentro de una lista un valor dado.
    Existe una manera de aumentar el rendimiento de la función (No funcional)
    Además, de hacer la función más usable (No funcional)
    Args:
        lista: lista con valores
        x: valor a buscar en la lista
    return:
        True: se ha encontrado el valor en la lista
        False: no se ha encontrado el valor en la lista
    """
    for elem in lista:
        if(elem == x):
           return True

    return False

def busqueda_lineal(lista, x):
    """Busqueda lineal
    Funcion que busca dentro de una lista un valor dado.
    Args:
        lista: lista con valores
        x: valor a buscar en la lista
    return:
        True: se ha encontrado el valor en la lista
        False: no se ha encontrado el valor en la lista
    """
    for elem in lista:
        if(elem == x):
            return True
    
    return False


if __name__ == "__main__":
    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    val = 20
    if(busqueda_lineal_mal(lista, val)):
        print(f"Se ha encontrado {val}")
    else:
        print(f"{val} no se encuentra en la lista")