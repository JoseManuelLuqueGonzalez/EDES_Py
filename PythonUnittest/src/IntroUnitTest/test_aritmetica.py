import unittest
import aritmetica as arit

class TestAritmetica(unittest.TestCase):

    #Especifico un test unitario para la funcion sumar
    def test_sumar(self):
        #Hemos querido comprobar si dos resultados eran iguales
        #Lo que esperabamos obtener y lo que obteníamos de verdad
        self.assertEqual(arit.suma(2,3), 5)
        self.assertEqual(arit.suma(4,6), 10)
        #self.assertEqual(arit.suma("a","b"), ValueError)
        #self.assertEqual(arit.suma("a",1), ValueError)
        self.assertEqual(arit.suma(0,-1), -1)
        self.assertEqual(arit.suma(1,-1), 0)
        self.assertEqual(arit.suma(-1,-1), -2)

if __name__ == "__main__":
    unittest.main()