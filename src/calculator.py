"""Calculadora"""


def suma(number_1, number_2):
    """Realiza una suma entre dos números"""
    return number_1 + number_2


def resta(number_1, number_2):
    """Realiza una resta entre dos números"""
    return number_1 - number_2


def multiplicacion(number_1, number_2):
    """Realiza una multiplicación entre dos números"""
    return number_1 * number_2


def division(number_1, number_2):
    """Realiza una división entre dos números"""

    if number_2 == 0:
        raise ValueError("No se puede dividir entre cero.")

    return number_1 / number_2
