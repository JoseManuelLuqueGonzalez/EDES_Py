def busqueda_binaria(lista, x):
    """
    Búsqueda binaria
    Precondición: lista está ordenada
    
    Busca en toda la lista dividiéndola en segmentos y considerando
    a la lista completa como el segmento que empieza en 0 y termina
    en len(lista) - 1.

    Devuelve -1 si x no está en lista;
    Devuelve p siendo p la posicion dentro de la lista, tal que lista[p] == x, si x está en lista
    """

    izq = 0 # izq guarda el índice inicio del segmento
    der = len(lista) -1 # der guarda el índice fin del segmento

    # un segmento es vacío cuando izq > der:
    while izq <= der:
        # el punto medio del segmento
        medio = int((izq+der)/2)

        # si el medio es igual al valor buscado, lo devuelve
        if lista[medio] == x:
            return medio

        # si el valor del punto medio es mayor que x, sigue buscando
        # en el segmento de la izquierda: [izq, medio-1], descartando la
        # derecha
        elif lista[medio] > x:
            der = medio-1

        # sino, sigue buscando en el segmento de la derecha:
        # [medio+1, der], descartando la izquierda
        else:
            izq = medio+1
        # si no salió del ciclo, vuelve a iterar con el nuevo segmento

    # salió del ciclo de manera no exitosa: el valor no fue encontrado
    return -1

# Código para probar la búsqueda binaria
def main():
    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    val = 9

    pos = busqueda_binaria(lista, val)

    if(pos==-1):
        print(f"El elemento {val} no se encuentra en la lista")
    else:
        print(f"El elemento {val} se encuentra en la posicion {pos} de la lista")

if __name__ == "__main__":
    main()