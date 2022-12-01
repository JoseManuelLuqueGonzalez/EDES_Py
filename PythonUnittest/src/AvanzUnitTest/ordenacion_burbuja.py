def burbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-(i+1)):
            if(lista[j] > lista[j+1]):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista


# Código para probar la ordenación por burbuja
def main():
    lista = [7,2,3,1,5,4,6]

    print(lista)

    burbuja(lista)

    print(lista)

if __name__ == "__main__":
    main()