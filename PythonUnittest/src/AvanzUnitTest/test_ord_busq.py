import unittest
import ordenacion_burbuja as ordenar
import busqueda_binaria as buscar

class TestOrdBusq(unittest.TestCase):
    
    def setUp(self):
        #Listas para ordenar y buscar
        self.lista1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.lista2 = [0,8,4,2,5,3,1,6,7]
        self.lista3 = [-6,-4,-5,-1,0,-2,-3]
        self.lista4 = [1,6,20,2,7,17,0,12,4]
        self.lista5 = ["a", "z", "m"]
        self.lista6 = [0]
        self.lista7 = [-1,1]
        self.lista8 = [-1,-1]
        self.lista9 = [1,1]
        self.lista10 = [0,0]

        #Listas para forzar errores en las pruebas
        self.listaBusqError = [7, 2, 5]

    def test_ordenacion(self):
        self.assertEqual(ordenar.burbuja(self.lista2), [0,1,2,3,4,5,6,7,8])
        self.assertEqual(ordenar.burbuja(self.lista5), ["a","m","z"])
        self.assertEqual(ordenar.burbuja(self.lista6), [0])
        self.assertEqual(ordenar.burbuja(self.lista7), [-1,1])
        self.assertEqual(ordenar.burbuja(self.lista8), [-1,-1])
        self.assertEqual(ordenar.burbuja(self.lista9), [1,1])
        self.assertEqual(ordenar.burbuja(self.lista10), [0,0])
        self.assertEqual(ordenar.burbuja(self.lista7), self.lista7)
        self.assertEqual(ordenar.burbuja(self.lista8), self.lista8)
        

    def test_sameObject(self):
        self.assertIs(ordenar.burbuja(self.lista2), self.lista2)
        self.assertIs(ordenar.burbuja(self.lista5), self.lista5)
        self.assertIs(ordenar.burbuja(self.lista7), self.lista7)
        
    
    """
    Podemos llegar a tener pruebas defectuosas, por lo que es imprescindible
    conocer bien las especificaciones, y conocer bien qué hace la función.
    """
    def test_busqueda_err1(self):
        #La primera es que, al haber declarado una lista desordenada pensamos que el método debe devolver -1
        #Pero, ¿Hay algo en la función que controle que la lista está ordenada?
        self.assertEqual(buscar.binaria(self.listaBusqError, 2), -1)
    
    def test_busqueda_err2(self):
        #La segunda es que, si no conocemos las especificaciones, podemos declararar la siguiente lista
        #[7, 2, 5]. Vemos que el numero que queremos buscar (el 2) está en la posición 1.
        #Así que hacemos una prueba para tal caso.
        self.assertEqual(buscar.binaria(self.listaBusqError, 2), 1)

if __name__ == "__main__":
    unittest.main()