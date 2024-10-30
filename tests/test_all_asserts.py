"""Consolidación de asserts"""
import unittest

class AllAssertsTest(unittest.TestCase):
    """Clase para entender los distintos tipos de asserts"""

    def test_assert_equal(self):
        """Validación de igualdad"""
        self.assertEqual(10, 10)
        self.assertEqual('Hola', 'Hola')

    def test_assert_true(self):
        """Validación de condiciones"""
        self.assertTrue(1 == 1)
        self.assertFalse(1 == 2)

    def test_assert_arraises(self):
        """Validación de las excepciones"""
        with self.assertRaises(ValueError):
            int('Hola, mundo')

    def test_assert_in(self):
        """Validación de que un elemento exista o no"""
        self.assertIn(13, [1, 2, 3, 13])
        self.assertNotIn(10, [1, 2, 3, 13])

    @unittest.skip('En pruebas')
    def test_skip(self):
        """Validación de prueba"""
        self.assertEqual('Hola', 'Mundo')
