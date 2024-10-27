"""Test de la calculadora"""
import unittest

from src import calculator


class CalculatorTests(unittest.TestCase):
    """
    Test para el script "calculator"
    """

    def test_suma(self):
        """
        Test para la función de suma
        """
        assert calculator.suma(2, 3) == 5

    def test_resta(self):
        """
        Test para la función de resta
        """
        assert calculator.resta(2, 3) == -1

    def test_multiplicacion(self):
        """
        Test para la función de multiplicación
        """
        assert calculator.multiplicacion(2, 3) == 6

    def test_division(self):
        """
        Test para la función de división cuando b no es cero.
        """
        assert calculator.division(6, 3) == 2

    def test_division_by_zero(self):
        """
        Test para la función de división en la que verificamos que se
        lanza un ValueError cuando b es cero
        """

        with self.assertRaises(ValueError):
            calculator.division(10, 0)
