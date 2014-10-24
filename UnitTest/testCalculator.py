#!/usr/bin/env python

import unittest
from Calculator import Calculator


class TestCalculator(unittest.TestCase):

    """# PRUEBAS DE SUMAS"""

    def test_suma_2_mas_2(self):
        '''self se refiere al mismo objeto/por convencion
        todos los metodos deben llevar test'''
        cal = Calculator()
        self.assertEqual(4, cal.summa(2, 2))

    def test_suma1_x_mas_y(self):
        cal = Calculator()
        self.assertEqual(23.5, cal.summa(20.0, 3.5))

    def test_suma2_x_mas_y(self):
        cal = Calculator()
        self.assertEqual(4, cal.summa(2, 2))
    '''# PRUEBAS DE RESTA'''

    def test_resta_30_menos_X(self):
        cal = Calculator()
        self.assertEqual(26.5, cal.resta(30, 3.5))

    def test_resta1_X_menos_Y(self):
        cal = Calculator()
        self.assertEqual(20, cal.resta(30, 10))

    def test_resta2_X_menos_Y(self):
        cal = Calculator()
        self.assertEqual(-52, cal.resta(-32, 20))
    '''# PRUEBAS DE DIVISION'''

    def test_divide_30_entre_10(self):
        cal = Calculator()
        self.assertEqual(3, cal.divide(30, 10))

    def test_divide1_X_entre_Y(self):
        cal = Calculator()
        self.assertEqual(2.5, cal.divide(250.0, 100.0))

    def test_divide2_X_entre_Y(self):
        cal = Calculator()
        self.assertEqual(11, cal.divide(33, 3))
    '''# PRUEBAS DE MULTIPLICACION'''

    def test_multiplica_4_por_15(self):
        cal = Calculator()
        self.assertEqual(60, cal.multiplica(4, 15))

    def test_multiplica1_X_por_Y(self):
        cal = Calculator()
        self.assertEqual(15, cal.multiplica(3, 5))

    def test_multiplica2_X_por_Y(self):
        cal = Calculator()
        self.assertEqual(6, cal.multiplica(3, 2))
if __name__ == "__main__":
    unittest.main()
