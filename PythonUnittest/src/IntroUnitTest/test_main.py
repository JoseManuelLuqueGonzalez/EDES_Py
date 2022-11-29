import suma as s
import unittest

class TestSuma(unittest.TestCase):

    """La conveción para declarar tests, es empezar por la palabra test"""
    def test_suma(self):
        self.assertEqual(s.suma(2,2), 4)
        self.assertEqual(s.suma(-1,1), 0)
        self.assertEqual(s.suma(-1,-1), -2)


if __name__ == "__main__":
    unittest.main()