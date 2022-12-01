import aritmetica as arit
import unittest

class TestAritmetica (unittest.TestCase):

    """La conveción para declarar tests, es empezar por la palabra test"""
    def test_suma(self):
        self.assertEqual(arit.suma(2,2), 4)
        self.assertEqual(arit.suma(-1,1), 0)
        self.assertEqual(arit.suma(-1,-1), -2)
    
    def test_div(self):
        with self.assertRaises(ValueError):
            arit.division(5,0)


if __name__ == "__main__":
    unittest.main()